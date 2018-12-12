import Interface as it
from Modelisation import Modele
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from JoueurHumain import JoueurHumain
from JoueurOrdi import JoueurOrdi

class Jeu():
    def __init__(self):
        
        self.modelisation = Modele()
        self.joueur = 1
        self.Joueur1 = JoueurHumain()
        self.Joueur2 = JoueurHumain()
        self.playing = True
        
        
        print("done")
             # creation d'un application
        app = QApplication([])  # on peut aussi passer en paramètre les arguments du programme sys.argv
        # creation d'une interface
        self.gui = it.GUI_Isohypses(self)
        # affichage de l'interface
        self.gui.show()
    
        # lancement de l'application
        r = app.exec_()

    def reception_clic(self, col, ligne):
        if (self.joueur == 1 and self.Joueur1.humain) or (self.joueur == 2 and self.Joueur2.humain) and self.playing:
            self.deplacer(col, ligne)

    def choix_clic(self, col):
        if self.joueur == 1:
            self.deplacer(col, 1)
        else :
            self.deplacer(col, 0)



    def deplacer(self, col, ligne):
        if ligne == 0:
            col = 5 - col
        indice = col + ligne * 7
        if ((self.joueur == 1 and ligne == 1) or (self.joueur == 2 and ligne == 0)) and self.modelisation.plateau[indice] != 0:
            retour = self.modelisation.jouer(indice)
            if self.modelisation.plateau[retour] == 1:
                if self.joueur == 1 and retour >= 7 and retour <= 12:
                    self.modelisation.vider(self.joueur, retour)
                elif self.joueur == 2 and retour >= 0 and retour <= 5:
                    self.modelisation.vider(self.joueur, retour)
            print(self.modelisation.plateau)
            print(self.modelisation.plateau[7:12])
            if self.modelisation.plateau[0:6] == [0,0,0,0,0,0]:
                nb = 0
                for i in range (6):
                    nb+= self.modelisation.plateau[i + 7]
                    self.modelisation.plateau[i + 7] = 0
                self.modelisation.plateau[13] += nb
                self.playing = False
            elif self.modelisation.plateau[7:13] == [0,0,0,0,0,0]:
                nb = 0
                for i in range (6):
                    nb+= self.modelisation.plateau[i]
                    self.modelisation.plateau[i] = 0
                self.modelisation.plateau[6] += nb
                self.playing = False
            self.gui.MAJ_val(self.modelisation.plateau)
            
            if (self.joueur == 1 and retour != 13) or (self.joueur == 2 and retour != 6):
                if self.joueur == 1:
                    self.joueur = 2
                    choix = self.Joueur2.jouer()
                else:
                    self.joueur = 1
                    choix = self.Joueur1.jouer()
        if self.joueur == 1:
            choix = self.Joueur1.jouer()
        else:
            choix = self.Joueur2.jouer()
        if choix != -1 and self.playing:
            self.choix_clic(choix)

if __name__ == "__main__":
    jeu = Jeu()
    