from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from JoueurHumain import JoueurHumain
from JoueurOrdi import JoueurOrdi
import Interface as it
import Jeu as j
import lancement as l
import sys


class FenetreFin(QWidget):
    
    def __init__(self, score, j2):
        QWidget.__init__(self)
        
        self.setWindowTitle("Fin de partie ")
        self.j2 = j2
        
        print(j2)

        # LAYOUT
        monLayout = QGridLayout()
         #placement des boutons, on donne le n° de ligne, le n° de colonne
         #et le nombre de lignes et de colonnes occupées
        
        nom1 = QLabel("J1")
        nom1.setFont(QFont("Arial", 16))
        nom1.setAlignment(Qt.AlignCenter)
        monLayout.addWidget(nom1, 0, 0, 1, 1)
        
        nom2 = QLabel("J2")
        nom2.setFont(QFont("Arial", 16))
        nom2.setAlignment(Qt.AlignCenter)
        monLayout.addWidget(nom2, 0, 1, 1, 1)
        
        score1 = QLabel(str(score[0]))
        score1.setFont(QFont("Arial", 20))
        score1.setAlignment(Qt.AlignCenter)
        monLayout.addWidget(score1, 1, 0, 1, 1)
        
        score2 = QLabel(str(score[1]))
        score2.setFont(QFont("Arial", 20))
        score2.setAlignment(Qt.AlignCenter)
        monLayout.addWidget(score2, 1, 1, 1, 1)
#        print(score)
#        self.b_rejouer_ = QPushButton("Rejouer")
#        self.b_rejouer_.setFont(QFont("Arial", 16))
#        self.b_rejouer_.clicked.connect(self.rejouer)
#        monLayout.addWidget(self.b_rejouer_, 3, 0, 1, 2)
#        
#        self.b_changer_ = QPushButton("Changer les paramètres")
#        self.b_changer_.setFont(QFont("Arial", 16))
#        self.b_changer_.clicked.connect(self.changer_param)
#        monLayout.addWidget(self.b_changer_, 4, 0, 1, 2)

        self.setLayout(monLayout)
        
    def rejouer(self):
        self.deleteLater()
        b2 = it.GUI_Kalaha()
        jeu = j.Jeu(b2, self.j2)
        b2.show()
    
    def changer_param(self):
        self.deleteLater()
        b2 = l.FenetreLancement()
        b2.show()
        
def main():
    app = QApplication([])

    gui = FenetreFin([40,9], JoueurOrdi(1))
    gui.show()

    r = app.exec()
    

if __name__ == "__main__":
    main()
    