from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import Interface

class QScene(QGraphicsScene):
    def __init__(self, x, y, wid, hgt, widget):
        QGraphicsScene.__init__(self, x, y, wid, hgt, widget)
        self.widget = widget
        

    def mousePressEvent(self, ev):
        
        if ev.button() == Qt.LeftButton:
            x, y = ev.scenePos().x(), ev.scenePos().y()
            for i in range (6):
                for j in range(2):
                    if ((x - (100 + 1000 / 9 * (i + 1))) ** 2 + (y - (50 + 400 / 8 + 400 / 8 * (4 * j))) ** 2) < 50 ** 2:
                        self.widget.bouger(i,j)
