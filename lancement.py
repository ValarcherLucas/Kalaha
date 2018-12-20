from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from JoueurHumain import JoueurHumain
from JoueurOrdi import JoueurOrdi
import lancement2 as l2
import Interface as it
import Jeu as j
import sys


class FenetreLancement(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Contre qui voulez vous jouer ? ")

        self.j2 = JoueurHumain()

        # LAYOUT
        monLayout = QGridLayout()
        # placement des boutons, on donne le n° de ligne, le n° de colonne
        # et le nombre de lignes et de colonnes occupées
        self.b1 = QRadioButton("Joueur contre Joueur")
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        monLayout.addWidget(self.b1)

        self.b2 = QRadioButton("Joueur contre Ordi")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        monLayout.addWidget(self.b2)
        
        self.b_valider_ = QPushButton("Valider")
        self.b_valider_.setFont(QFont("Arial", 16))
        self.b_valider_.clicked.connect(self.launch_next)
        monLayout.addWidget(self.b_valider_)

        self.setLayout(monLayout)

    def btnstate(self, b):
        """
        Fonction permettant de changer un paramètre selon la valeur dans le RadioButton

        :param b: radiobutton
        :return:
        """

        if b.text() == "Joueur contre Joueur":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.j2 = JoueurHumain()

        if b.text() == "Joueur contre Ordi":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.j2 = JoueurOrdi(0)
    
    def launch_next(self):
        """
        Fonction permettant de lancer la fenêtre suivante
        :return:
        """

        if self.j2.humain:
            self.deleteLater()
            b2 = it.GUI_Kalaha()
            jeu = j.Jeu(b2, self.j2)
            b2.show()
            
        else:
            self.deleteLater()
            b2 = l2.FenetreLancement2()
            b2.show()
            
            


def main():
    app = QApplication([])

    gui = FenetreLancement()
    gui.show()

    r = app.exec()


if __name__ == "__main__":
    main()