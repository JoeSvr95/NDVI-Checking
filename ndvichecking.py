import sys
import numpy as np
import cv2

from views.ndvi_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QStatusBar
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen

class MainNDVI(Ui_MainWindow, QMainWindow):
    def __init__(self): # Inicializa todos los atributos y los widgets
        super(MainNDVI, self).__init__()
        self.setupUi(self)
        self.lastPoint = QPoint()
        self.firstPoint = QPoint()
        self.select = False
        self.drawing = False
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.loadImgBtn.clicked.connect(self.setImage)
        self.selectBtn.clicked.connect(self.startSelectROI)
        self.imageLbl.mousePressEvent = self.selectRegion
        self.imageLbl.mouseMoveEvent = self.drawingSelection
        self.imageLbl.mouseReleaseEvent = self.completeROI

    # Método para colocar una imágen
    def setImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QPixmap(fileName)
            #pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)
            size = pixmap.size()
            self.drawing = False
            self.fileName = fileName
            self.imageLbl.setPixmap(pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
            self.statusBar.showMessage("Resolución: " + str(size.width()) + "x" + str(size.height()))

    # Método para habilitar la opción de selección
    def startSelectROI(self):
        self.imageLbl.paintEvent = self.selecROI
        self.imageLbl.setCursor(Qt.CrossCursor)
        self.select = True

    # Crea el objeto painter
    def selecROI(self, event):
        painter = QPainter(self)

    # Al hacer click se empieza a dibujar
    def selectRegion(self, event):
        if event.button() == Qt.LeftButton and self.select:
            self.drawing = True
            self.lastPoint = event.pos()
            self.firstPoint = event.pos()

    # Al mover el mouse se dibuja el paso del mouse
    def drawingSelection(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.imageLbl.pixmap())
            painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.imageLbl.update()
    
    # Si el usuario no ha completado una figura cerrada
    # Esta función completa la figura
    def completeROI(self, event):
        if self.drawing:
            painter = QPainter(self.imageLbl.pixmap())
            painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))
            painter.drawLine(self.firstPoint, self.lastPoint)
            self.imageLbl.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainNDVI()
    widget.show()
    sys.exit(app.exec_())
