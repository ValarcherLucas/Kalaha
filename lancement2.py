from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import Interface as it
import Jeu as j
from JoueurOrdi import JoueurOrdi


class FenetreLancement2(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Contre qui voulez vous jouer ? ")

        self.j2 = JoueurOrdi(0)

        # LAYOUT
        monLayout = QGridLayout()
        # placement des boutons, on donne le n° de ligne, le n° de colonne
        # et le nombre de lignes et de colonnes occupées
        
        self.b1 = QRadioButton("Très Facile")
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        monLayout.addWidget(self.b1)

        self.b2 = QRadioButton("Facile")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        monLayout.addWidget(self.b2)
        
        self.b3 = QRadioButton("Moyen")
        self.b3.toggled.connect(lambda: self.btnstate(self.b3))
        monLayout.addWidget(self.b3)
        
        self.b4 = QRadioButton("Difficile")
        self.b4.toggled.connect(lambda: self.btnstate(self.b4))
        monLayout.addWidget(self.b4)
        
        self.setWindowTitle("RadioButton demo")
        
        self.b_valider_ = QPushButton("Valider")
        self.b_valider_.setFont(QFont("Arial", 16))
        self.b_valider_.clicked.connect(self.launch_next)
        monLayout.addWidget(self.b_valider_)

        self.setLayout(monLayout)

    def btnstate(self, b):

        if b.text() == "Très Facile":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.j2 = JoueurOrdi(0)

        if b.text() == "Facile":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.j2 = JoueurOrdi(1)
        
        if b.text() == "Moyen":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.j2 = JoueurOrdi(2)
                
        if b.text() == "Difficile":
            if b.isChecked() == True:
                print(b.text() + " is selected")
                self.j2 = JoueurOrdi(3)
    
    def launch_next(self):
        self.deleteLater()
        b2 = it.GUI_Kalaha()
        jeu = j.Jeu(b2, self.j2)
        b2.show()
                
def main():
    app = QApplication([])

    gui = FenetreLancement2()
    gui.show()

    r = app.exec()
    

if __name__ == "__main__":
    main()
    