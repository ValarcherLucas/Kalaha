from Joueur import Joueur
from random import *
class JoueurOrdi(Joueur):
    def __init__(self, difficulty):
        self.humain = False
        self.difficulty = difficulty
        self.nb_vision = (difficulty - 1) ** 2 * 2

    def jouer(self, modele, joueur):
        """
        Fonction appelé pour obtenir un coup à jouer
        :param modele: modèle des données
        :param joueur: numéro du joueur en cours
        :return: coup à jouer sous forme de colonne
        """
        #Si la difficulté est à 0 l'ordi joue au hasard
        if self.difficulty == 0:
            return randint(0, 5)
            
        else:
            meilleur_coup, plateau = self.meilleur_choix(modele, joueur)
            print(plateau)
            # On transforme l'index en colonne afin de le transmettre
            return 5 - meilleur_coup
            
    def meilleur_choix(self, modele, joueur, coup_d_avance = 0):
        print(coup_d_avance)
        """
        Algorithme permettant de trouver le meilleur coup pour le tour suivant
        :param modele: modèle des données
        :param joueur: numéro du joueur en cours
        :return: coup à jouer sous forme d'index
        """
        choix = {}
        plateau_result = {}
        for i in range(6):
            if modele[i] != 0:
                retour, plateaun = self.depl(i + (2 -joueur) * 7, modele.copy())
                plateaun = self.test_dernier(retour, joueur, plateaun)
                continu, plateaun = self.fin(plateaun)
                rejouer = self.rejouer(retour, joueur)
                if rejouer and continu:
                    #Si on rejoue on part sur un processus récursif
                    #Le résultat de plateau final sera alors le plateau après tous les coups rejoués
                    choix_suiv, plateaun = self.meilleur_choix(plateaun, joueur, coup_d_avance)
                
                if coup_d_avance < self.nb_vision and continu:
                    choix_suiv, plateaun = self.meilleur_choix(plateaun,2 - (joueur - 1), coup_d_avance + 1)
                #On évalue pour tout les coups la valeur du coup
                choix[i] = (self.evaluer(modele, plateaun, joueur))
                plateau_result[i] = plateaun
                
        maxi = - 5000
        mieux = 0
        #On regarde parmi les coups la valeur la plus élevée
        for (k, v) in zip(choix.keys(), choix.values()):
            if v > maxi:
                mieux = k
                maxi = v
        # retour, plateauf = self.depl(mieux, modele.copy())
        # plateauf = self.test_dernier(retour, joueur, plateauf)
        # fini, plateauf = self.fin(plateauf)
        return(mieux, plateau_result[mieux])
        
            
    def depl(self, indice, plateau):
        """
        Fonction pour déplacer les pions dans une case donnée vers les cases suivantes
        :param indice: case à vider
        :param plateau: état du plateau
        :return retour: dernière case jouée
        :return plateau: état du plateau modifié
        """
        #On récupère le nombre de pions dans la case initiale
        nb = plateau[indice]
        plateau[indice] = 0
        retour = 0
        #On place un pion par un pion dans les cases suivantes
        for i in range(nb):
            pos = i + indice + 1
            while pos > len(plateau) - 1:
                pos -= len(plateau)
            plateau[pos] += 1
            retour = pos
        return retour, plateau
        
    def evaluer(self, ancien_plateau, nouveau_plateau, joueur):
        """
        Evaluation des scores entre deux plateau différents

        :param ancien_plateau: ancien plateau
        :param nouveau_plateau: nouveau plateau
        :param joueur: joueur qui vient de jouer
        :return result: score
        """
        if joueur == 1:
            result = (nouveau_plateau[13] - ancien_plateau[13])- (nouveau_plateau[6] - ancien_plateau[6])
        else:
            result = (nouveau_plateau[6] - ancien_plateau[6])- (nouveau_plateau[13] - ancien_plateau[13])
        return result
        
    def test_dernier(self, retour, joueur, plateau):
        """
        Fonction vérifiant si le dernier coup a été joué dans une case auparavant vide

        :param retour: dernière case
        :param joueur: joueur qui vient de jouer
        :param plateau: plateau
        :return: plateau modifié
        """
        if plateau[retour] == 1:
                if joueur == 1 and retour >= 7 and retour <= 12:
                    self.vider(joueur, retour, plateau)
                elif joueur == 2 and retour >= 0 and retour <= 5:
                    self.vider(joueur, retour, plateau)
        return plateau
        
    def vider(self, joueur, case, plateau):
        """
        Fonction permettant de vider une case et sa case opposé et de placer les pions récupérer dans le kalaha

        :param joueur: joueur qui vient de jouer
        :param case: case à vider
        :param plateau: plateau
        :return:
        """
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
        """
        Fonction pour vérifier si les conditions de fin de partie sont réunis
        :param plateau: plateau
        :return bool: True si le jeu est fini, sinon False
        :return plateau: plateau final
        """
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
        """
        Fonction qui vérifie si le joueur doit rejouer
        :param retour: dernière case jouée
        :param joueur: joueur qui vient de jouer
        :return:
        """
        if (joueur == 1 and retour == 13) or (joueur == 2 and retour == 6):
            return True
        else:
            return False


if __name__ == "__main__":
    j2 = JoueurOrdi(1)
    print(j2.jouer([4, 4, 4, 4, 4, 1, 0, 4, 4, 4, 4, 4, 4, 0], 2))
    
    print(j2.jouer([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 2))
    
    j2 = JoueurOrdi(2)
    print(j2.jouer([4, 4, 4, 9, 3, 1, 0, 3, 0, 4, 0, 4, 4, 0], 2))
    



