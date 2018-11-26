from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from QScene import *

# definition d'une GUI
class GUI_Isohypses(QWidget):
    def __init__(self, jeu):
        # on crée la fenêtre graphique
        QWidget.__init__(self)
        self.setWindowTitle("Kalaha")
        wid, hgt = 1000, 400
        self.scene_ = QScene(0, 0, wid, hgt, self)
        self.view_= QGraphicsView(self.scene_, self)
        self.view_.setMinimumSize(wid + 100, hgt + 100)
        self.scene_.addLine(0, hgt / 2, wid, hgt / 2)
        self.scene_.addLine(0, 0, 0, hgt)
        self.scene_.addLine(0, 0, wid, 0)
        self.scene_.addLine(0, hgt, wid, hgt)
        self.scene_.addLine(wid, 0, wid, hgt)
        self.jeu = jeu
        
        self.liste_texte = [0 for i in range (14)]

        for i in range(12):
            if i<6:
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
        self.jeu.reception_clic(col, ligne)
        
    def MAJ_val(self, liste_val):
        for i in range(14):
            self.liste_texte[i].setPlainText(str(liste_val[i]))
            
        


def main():
    # creation d'un application
    app = QApplication([])  # on peut aussi passer en paramètre les arguments du programme sys.argv
    # creation d'une interface
    gui = GUI_Isohypses()
    # affichage de l'interface
    gui.show()

    # lancement de l'application
    r = app.exec_()
    
    
if __name__ == "__main__":
    main()