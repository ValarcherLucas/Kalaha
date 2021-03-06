from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from QScene import *
from PyQt5 import QtTest
from JoueurHumain import JoueurHumain
import sys


# definition d'une GUI
class GUI_Kalaha(QWidget):
    """
    Classe permettant de visualiser l'état du jeu et d'interagir avec celui-ci
    """
    def __init__(self):
        # Création de la fenètre avec ses paramètres basiques
        QWidget.__init__(self)
        self.setWindowTitle("Kalaha")
        wid, hgt = 1000, 400
        self.scene_ = QScene(0, 0, wid, hgt, self)
        self.view_= QGraphicsView(self.scene_, self)
        self.view_.setMinimumSize(wid + 100, hgt + 100)
        #self.scene_.addLine(0, hgt / 2, 50, hgt / 2)
        #self.scene_.addLine(50 + wid / 9 * 7 + hgt / 4 , hgt / 2, wid, hgt / 2)
        #self.scene_.addLine(50 + hgt / 4, hgt / 2, 50 + wid / 9 * 7, hgt / 2)
        
        
#        monLayout = QGridLayout()
#        self.b_valider_ = QPushButton("Valider")
#        self.b_valider_.setFont(QFont("Arial", 16))
#        self.b_valider_.clicked.connect(self.endgame)
#        monLayout.addWidget(self.b_valider_)
#        self.setLayout(monLayout)

        
        # Dessin des contours de la zone de jeu
        self.scene_.addLine(0, 0, 0, hgt)
        self.scene_.addLine(0, 0, wid, 0)
        self.scene_.addLine(0, hgt, wid, hgt)
        self.scene_.addLine(wid, 0, wid, hgt)

        # Initialisation des paramètres pour gérer l'affichage
        self.jeu = 0
        self.rendering = False
        self.liste_texte = [0 for i in range (14)]

        # Création des 12 zones de jeu
        # Une zone est représenté par un rond et un texte
        # Un premier test rajoutait un bouton sur les zones afin de les rendre cliquables
        for i in range(12):
            if i<6:
                # On crée des ronds de 100 unités de rayon espacés de 111 unités pour la première ligne
                self.scene_.addEllipse(50 + wid / 9 * (i + 1), hgt / 8, hgt / 4, hgt / 4)
                text = self.scene_.addText("4")
                text.setPos(100 + wid / 9 * (i + 1), 50 + hgt / 8)
                self.liste_texte[5-i] = text
#                txt = QLabel("4", self)
#                txt.setDisabled(True)
#                txt.setAlignment(Qt.AlignCenter)
#                txt.setWordWrap(True)
#                self.scene_.addWidget(txt)
#                txt.setGeometry(100 + wid / 9 * (i + 1), 50 + hgt / 8, hgt / 4, hgt / 4)
#                self.liste_texte[5-i] = txt
            else:
                # On crée des ronds de 100 unités de rayon espacés de 111 unités pour la seconde ligne
                self.scene_.addEllipse(50 + wid / 9 * (i - 5), hgt / 8 * 5, hgt / 4, hgt / 4)
                text = self.scene_.addText("4")
                text.setPos(100 + wid / 9 * (i - 5), 50 + hgt / 8 * 5)
                self.liste_texte[i + 1] = text
                #txt = QLabel("4", self)
                #txt.setDisabled(True)
                #txt.setAlignment(Qt.AlignCenter)
                #txt.setWordWrap(True)
                #self.scene_.addWidget(txt)
                #txt.setGeometry(100 + wid / 9 * (i - 5), 50 + hgt / 8 * 5, hgt / 4, hgt / 4)
                #self.liste_texte[i + 1] = txt


        # On crée les rectangles de la même manière
        self.scene_.addRect(50, hgt / 8 - 10, hgt / 4, hgt - (hgt / 8 - 10) * 2)
        text = self.scene_.addText("0")
        text.setPos(100, 150 + hgt / 8 - 10)
        self.liste_texte[6] = text
#        txt = QLabel("1", self)
#        txt.setAlignment(Qt.AlignCenter)
#        txt.setWordWrap(True)
#        self.scene_.addWidget(txt)
#        txt.setGeometry(50, hgt / 8 - 10, hgt / 4, hgt - (hgt / 8 - 10) * 2)
#        self.liste_texte[6] = txt


        self.scene_.addRect(50 + wid / 9 * 7, hgt / 8 - 10, hgt / 4, hgt - (hgt / 8 - 10) * 2)
        text = self.scene_.addText("0")
        text.setPos(100 + wid / 9 * 7, 150 + hgt / 8 - 10)
        self.liste_texte[13] = text
#        txt = QLabel("1", self)
#        txt.setAlignment(Qt.AlignCenter)
#        txt.setWordWrap(True)
#        self.scene_.addWidget(txt)
#        txt.setGeometry(50 + wid / 9 * 7, hgt / 8 - 10, hgt / 4, hgt - (hgt / 8 - 10) * 2)
#        self.liste_texte[13] = txt




    def bouger(self, col, ligne):
        """
        Fonction permettant le lancement d'un coup sans contrôle

        :param col: colonne du clic
        :param ligne: ligne du clic
        :return:
        """
        self.jeu.reception_clic(col, ligne)
        
    def MAJ_val(self, liste_val, indice):
        """
        Fonction mettant à jour l'interface en deux temps
        Dans le premier temps le coup est rejouée et les valeur affichée en rouge, puis les valeurs sont mises à jour
        pour inclure les changements liés au règles de vidages des trous

        :param liste_val: valeurs obtenues après le coup
        :param indice: place où le coup a été jouée
        :return:
        """
        rendering = True
        nb_p = int(self.liste_texte[indice].toPlainText())
        self.liste_texte[indice].setPlainText("0")
        
        self.liste_texte[indice].setDefaultTextColor(QColor(255, 0, 0))
        for i in range(nb_p):
            pos = i + indice + 1
            while pos > len(self.liste_texte) - 1:
                pos -= len(self.liste_texte)
                print(pos) #à ne pas suppr bug sinon
            self.liste_texte[pos].setPlainText(str(int(self.liste_texte[pos].toPlainText()) + 1))
            self.liste_texte[pos].setDefaultTextColor(QColor(255, 0, 0))
            QtTest.QTest.qWait(250)
        QtTest.QTest.qWait(1000)
        for i in range(14):
            self.liste_texte[i].setPlainText(str(liste_val[i]))
            self.liste_texte[i].setDefaultTextColor(QColor(0, 0, 0))
        rendering = False
    
    def setJeu(self, jeu):
        self.jeu = jeu
        
    def endgame(self):
        print("salut")
        import fin as f
        self.deleteLater()
        b2 = f.FenetreFin(score, JoueurHumain())
        b2.show()
        print("test") #Pas réussi à faire s'afficher autrement l'écran de fon qu'avec ces deux print succesifs
        print(b2.score)
        
            
            
        


def main():
    # creation d'un application
    app = QApplication([])  # on peut aussi passer en paramètre les arguments du programme sys.argv
    # creation d'une interface
    gui = GUI_Kalaha()
    # affichage de l'interface
    gui.show()

    # lancement de l'application
    r = app.exec_()
    
    
    
    
    
    
if __name__ == "__main__":
    main()