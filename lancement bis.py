from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class lancement(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.setWindowTitle("Quelle partie choisissez-vous?")
    wid, hgt = 400,400
    self.scene_ = GGraphicsScene(0,0,wid,hgt,self)
    self.view_ = QGraphicsView(self.scene_, self)
    self.view_.setMinimumSize(wid + 100, hgt + 100)
    self.scene_.addLine(0, hgt / 2, wid, hgt / 2)
    self.scene_.addLine(0, 0, 0, hgt)
    self.scene_.addLine(0, 0, wid, 0)
    self.scene_.addLine(0, hgt, wid, hgt)
    self.scene_.addLine(wid, 0, wid, hgt)
    
    self.scene_.addRect(hgt/2,hgt,wid,-hgt/2)
    self.scene_.addRect(0,hgt/2,wid,-hgt/2)
