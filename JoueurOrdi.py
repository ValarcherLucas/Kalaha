from Joueur import Joueur
from random import *
class JoueurOrdi(Joueur):
    def __init__(self, difficulty):
        self.humain = False
        self.difficulty = difficulty

    def jouer(self, modele, joueur):
        print("coucou")
        if self.difficulty == 0:
            return randint(0, 5)
            
        else:
            meilleur_coup, plateau = self.meilleur_choix(modele, joueur)
            return 5 - meilleur_coup
            
    def meilleur_choix(self, modele, joueur):
        choix = {}
        plateau_result = {}
        for i in range(6):
            if modele[i] != 0:
                retour, plateaun = self.depl(i, modele.copy())
                plateaun = self.test_dernier(retour, joueur, plateaun)
                fini, plateaun = self.fin(plateaun)
                rejouer = self.rejouer(retour, joueur)
                if rejouer:
                    choix_suiv, plateaun = self.meilleur_choix(plateaun, joueur)
                choix[i] = (self.evaluer(modele, plateaun, joueur))
                plateau_result[i] = plateaun
                
        maxi = - 5000
        mieux = 0
        for (k, v) in zip(choix.keys(), choix.values()):
            if v > maxi:
                mieux = k
                maxi = v
        retour, plateauf = self.depl(mieux, modele.copy())
        plateauf = self.test_dernier(retour, joueur, plateauf)
        fini, plateauf = self.fin(plateauf)
        return(mieux, plateau_result[mieux])
        
            
    def depl(self, indice, plateau):
        nb = plateau [indice]
        plateau[indice] = 0
        retour = 0
        for i in range(nb):
            pos = i + indice + 1
            while pos > len(plateau) - 1:
                pos -= len(plateau)
            plateau[pos] += 1
            retour = pos
        return retour, plateau
        
    def evaluer(self, ancien_plateau, nouveau_plateau, joueur):
        if joueur == 1:
            result = (nouveau_plateau[13] - ancien_plateau[13])- (nouveau_plateau[6] - ancien_plateau[6])
        else:
            result = (nouveau_plateau[6] - ancien_plateau[6])- (nouveau_plateau[13] - ancien_plateau[13])
        return result
        
    def test_dernier(self, retour, joueur, plateau):
        if plateau[retour] == 1:
                if joueur == 1 and retour >= 7 and retour <= 12:
                    self.vider(joueur, retour, plateau)
                elif joueur == 2 and retour >= 0 and retour <= 5:
                    self.vider(joueur, retour, plateau)
        return plateau
        
    def vider(self, joueur, case, plateau):
        if joueur == 1:
            nb1 = plateau[case]
            nb2 = plateau[case - 7]
            plateau[case] = 0
            plateau[case - 7] = 0
            plateau[13] += nb1 + nb2
        if joueur == 2:
            nb1 = plateau[case]
            nb2 = plateau[case + 7]
            plateau[case] = 0
            plateau[case + 7] = 0
            plateau[6] += nb1 + nb2
    
    def fin(self, plateau):
        if plateau[0:6] == [0,0,0,0,0,0]:
                nb = 0
                for i in range (6):
                    nb+= plateau[i + 7]
                    plateau[i + 7] = 0
                plateau[13] += nb
                return False, plateau
        elif plateau[7:13] == [0,0,0,0,0,0]:
            nb = 0
            for i in range (6):
                nb+= plateau[i]
                plateau[i] = 0
            plateau[6] += nb
            return False, plateau
        return True, plateau
        
    def rejouer(self, retour, joueur):
        if (joueur == 1 and retour == 13) or (joueur == 2 and retour == 6):
            return True
        else:
            return False


if __name__ == "__main__":
    j2 = JoueurOrdi(1)
    j2.jouer([4, 4, 4, 4, 4, 1, 0, 4, 4, 4, 4, 4, 4, 0], 2)
    



