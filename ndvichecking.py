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
        self.loadRGBBtn.clicked.connect(self.loadRGBImage)
        self.loadNDVIBtn.clicked.connect(self.loadNDVIImage)
        self.selectBtn.clicked.connect(self.selectROI)
        #self.opencvBtn.clicked.connect(self.opencvFunc)

    # Método para colocar una imágen
    def loadRGBImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        if fileName:
            pixmap = QPixmap(fileName)
            #pixmap = pixmap.scaled(self.ndvi_view.width(), self.ndvi_view.height(), QtCore.Qt.KeepAspectRatio)
            size = pixmap.size()
            self.rgb_view.setImage(pixmap)
            self.statusBar.showMessage("Resolución: " + str(size.width()) + "x" + str(size.height()))
    
    def loadNDVIImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        if fileName:
            pixmap = QPixmap(fileName)
            #pixmap = pixmap.scaled(self.ndvi_view.width(), self.ndvi_view.height(), QtCore.Qt.KeepAspectRatio)
            size = pixmap.size()
            self.ndvi_view.setImage(pixmap)
            self.statusBar.showMessage("Resolución: " + str(size.width()) + "x" + str(size.height()))

    # Método para habilitar la opción de selección
    def selectROI(self):
        self.rgb_view.startSelectROI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainNDVI()
    widget.show()
    sys.exit(app.exec_())
