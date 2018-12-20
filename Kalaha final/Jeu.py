import Interface as it
from Modelisation import Modele
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from JoueurHumain import JoueurHumain
from JoueurOrdi import JoueurOrdi
from PyQt5 import QtTest
from Interface import GUI_Kalaha

class Jeu():
    """
    Classe principale reliant les classes entre elles
    """
    def __init__(self, gui, j2):
        
        self.gui = gui
        self.modelisation = Modele()
        self.joueur = 1
        self.Joueur1 = JoueurHumain()
        self.Joueur2 = j2
        self.playing = True
        self.wait = False
        print(self.gui.jeu)
        
        self.gui.jeu = self
        
        print("ca va")

    def reception_clic(self, col, ligne):
        """
        Commande à effectuer lorsqu'un clic est réalisé sur une des zones de jeu

        :param col: colonne du clic
        :param ligne: ligne du clic
        :return:
        """

        #Seul un joueur humain peut cliquer on ne valide donc le passage que si c'est au tour d'un joueur humain
        if (self.joueur == 1 and self.Joueur1.humain) or (self.joueur == 2 and self.Joueur2.humain) and self.playing:
            self.deplacer(col, ligne)

    def choix_clic(self, col):
        """
        Commande à effectuer dans le cas d'un choix d'ordinateur

        :param col: Colonne désiré
        :return:
        """
        # L'ordinateur envoie seulement la colonne et selon sa place on prend la ligne selon sa place
        if self.joueur == 1:
            self.deplacer(col, 1)
        else :
            self.deplacer(col, 0)



    def deplacer(self, col, ligne):
        """
        Fonction qui accomplit le déplacement d'une case et des étapes de vérification qui suivent

        :param col: colonne où jouer
        :param ligne: ligne où jouer
        :return:
        """

        #La variable choix permet de visualiser le choix de case si un ordi joue
        #Il vaut -2 si il n'a pas été encore réalisé et -1 si c'est à un humain de jouer
        choix = -2
        if ligne == 0:
            # L'indexation est en sens inverse sur la ligne supérieur on corrige donc cela
            col = 5 - col

        # On obtient alors la position de la case dans la liste
        indice = col + ligne * 7
        #On vérifie que l'on a le droit de jouer
        #Le coup doit être sur la bonne ligne
        #La case ne doit pas être vide
        #Le rendu doit être fini
        if ((self.joueur == 1 and ligne == 1) or (self.joueur == 2 and ligne == 0)) and self.modelisation.plateau[indice] != 0 and not self.wait:
            self.wait = True
            retour = self.modelisation.jouer(indice)
            self.modelisation.test_dernier(retour, self.joueur)
            self.playing = self.modelisation.fin()
            self.gui.MAJ_val(self.modelisation.plateau, indice)
            
            while self.gui.rendering:
                pass
            QtTest.QTest.qWait(2000)
            #Si on a ces conditions on joue normalement, sinon le joueur doit rejouer
            if ((self.joueur == 1 and retour != 13) or (self.joueur == 2 and retour != 6))  and self.playing:
                if self.joueur == 1:
                    self.joueur = 2
                    choix = self.Joueur2.jouer(self.modelisation.plateau.copy(), self.joueur)
                else:
                    self.joueur = 1
                    choix = self.Joueur1.jouer(self.modelisation.plateau.copy(), self.joueur)
            self.wait = False
        #On ne rentre que si un choix n'a pas été prit
        if self.joueur == 1 and choix == -2 and self.playing:
            choix = self.Joueur1.jouer(self.modelisation.plateau.copy(), self.joueur)
        elif choix == -2 and self.playing:
            choix = self.Joueur2.jouer(self.modelisation.plateau.copy(), self.joueur)
        
        
        if choix != -1 and self.playing:
            self.choix_clic(choix)
        if not self.playing:
            
            
            score = [self.modelisation.plateau[13], self.modelisation.plateau[6]]
            #self.gui.endgame(score, self.Joueur2)
            
if __name__ == "__main__":
    app = QApplication([])

    gui = GUI_Kalaha()
    jeu = Jeu(gui, JoueurHumain())
    gui.show()

    r = app.exec()
    
    
    