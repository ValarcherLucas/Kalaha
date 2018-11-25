import Interface as it
from Modelisation import Modele
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Jeu():
    def __init__(self):
        
        self.modelisation = Modele()
        self.joueur = 1
        
        
        print("done")
             # creation d'un application
        app = QApplication([])  # on peut aussi passer en paramètre les arguments du programme sys.argv
        # creation d'une interface
        self.gui = it.GUI_Isohypses(self)
        # affichage de l'interface
        self.gui.show()
    
        # lancement de l'application
        r = app.exec_()

    def déplacer(self, col, ligne):
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
            self.gui.MAJ_val(self.modelisation.plateau)
            
            if (self.joueur == 1 and retour != 13) or (self.joueur == 2 and retour != 6):
                if self.joueur == 1:
                    self.joueur = 2
                else:
                    self.joueur = 1

if __name__ == "__main__":
    jeu = Jeu()
    