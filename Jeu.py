import Interface as it
from Modelisation import Modele
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from JoueurHumain import JoueurHumain
from JoueurOrdi import JoueurOrdi
from PyQt5 import QtTest

class Jeu():
    def __init__(self):
        
        self.modelisation = Modele()
        self.joueur = 1
        self.Joueur1 = JoueurHumain()
        self.Joueur2 = JoueurOrdi(1)
        self.playing = True
        self.wait = False
        
        
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
        choix = -2
        if ligne == 0:
            col = 5 - col
        indice = col + ligne * 7
        if ((self.joueur == 1 and ligne == 1) or (self.joueur == 2 and ligne == 0)) and self.modelisation.plateau[indice] != 0 and not self.wait:
            self.wait = True
            retour = self.modelisation.jouer(indice)
            self.modelisation.test_dernier(retour, self.joueur)
            self.playing = self.modelisation.fin()
            self.gui.MAJ_val(self.modelisation.plateau, indice)
            
            while self.gui.rendering:
                pass
            QtTest.QTest.qWait(2000)
            if (self.joueur == 1 and retour != 13) or (self.joueur == 2 and retour != 6):
                if self.joueur == 1:
                    print("a")
                    self.joueur = 2
                    choix = self.Joueur2.jouer(self.modelisation.plateau.copy(), self.joueur)
                else:
                    print("b")
                    self.joueur = 1
                    choix = self.Joueur1.jouer(self.modelisation.plateau.copy(), self.joueur)
            self.wait = False
        if self.joueur == 1 and choix == -2:
            print("c")
            choix = self.Joueur1.jouer(self.modelisation.plateau.copy(), self.joueur)
        elif choix == -2:
            print("d")
            choix = self.Joueur2.jouer(self.modelisation.plateau.copy(), self.joueur)
            print(choix)
        print(self.modelisation.plateau)
        
        
        if choix != -1 and self.playing:
            self.choix_clic(choix)
            
if __name__ == "__main__":
    jeu = Jeu()
    