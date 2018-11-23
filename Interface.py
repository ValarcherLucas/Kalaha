from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# definition d'une GUI
class GUI_Isohypses(QWidget):
    def __init__(self):
        # on crée la fenêtre graphique
        QWidget.__init__(self)
        self.setWindowTitle("Kalaha")
        wid, hgt = 1000, 400
        self.scene_ = QGraphicsScene(0, 0, wid, hgt, self)
        self.view_= QGraphicsView(self.scene_, self)
        self.view_.setMinimumSize(wid + 100, hgt + 100)
        self.scene_.addLine(0, hgt / 2, wid, hgt / 2)
        self.scene_.addLine(0, 0, 0, hgt)
        self.scene_.addLine(0, 0, wid, 0)
        self.scene_.addLine(0, hgt, wid, hgt)
        self.scene_.addLine(wid, 0, wid, hgt)

        for i in range(12):
            if i<6:
                self.scene_.addEllipse(50 + wid / 9 * (i + 1), hgt / 8, hgt / 4, hgt / 4 )
            else:
                self.scene_.addEllipse(50 + wid / 9 * (i - 5), hgt / 8 * 5, hgt / 4, hgt / 4)
                b1 = QPushButton()
                b1.clicked.connect(partial(self.bouger, i))
                b1.name = i
                b1.setGeometry(50 + wid / 9 * (i - 5), hgt / 8 * 5, hgt / 4, hgt / 4)
                b1.setVisible(True)
                self.scene_.addWidget(b1)

        self.scene_.addRect(50, hgt / 8 - 10, hgt / 4, hgt - (hgt / 8 - 10) * 2)
        self.scene_.addRect(50 + wid / 9 * 7, hgt / 8 - 10, hgt / 4, hgt - (hgt / 8 - 10) * 2)



    def bouger(self, int):
        print(int)


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