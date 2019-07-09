import sys
import numpy as np
import cv2

from views.ndvi_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QStatusBar
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen

class MainNDVI(Ui_MainWindow, QMainWindow):
    def __init__(self): # Inicializa todos los atributos y los widgets
        super(MainNDVI, self).__init__()
        self.setupUi(self)
        self.loadRGBBtn.clicked.connect(self.loadRGBImage)
        self.loadNDVIBtn.clicked.connect(self.loadNDVIImage)
        self.selectBtn.clicked.connect(self.selectROI)
        self.opencvBtn.clicked.connect(self.opencvFunc)

    # Método para colocar una imágen
    def loadRGBImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        if fileName:
            pixmap = QPixmap(fileName)
            file_info = QFileInfo(fileName)
            #pixmap = pixmap.scaled(self.ndvi_view.width(), self.ndvi_view.height(), QtCore.Qt.KeepAspectRatio)
            size = pixmap.size()
            self.rgb_view.setImage(pixmap)
            self.rgb_info.setText("Resolución: " + str(size.width()) + "x" + str(size.height()) + ", Tamaño: " + str(file_info.size()))
    
    def loadNDVIImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        if fileName:
            pixmap = QPixmap(fileName)
            file_info = QFileInfo(fileName)
            #pixmap = pixmap.scaled(self.ndvi_view.width(), self.ndvi_view.height(), QtCore.Qt.KeepAspectRatio)
            size = pixmap.size()
            self.ndvi_view.setImage(pixmap)
            self.ndvi_info.setText("Resolución: " + str(size.width()) + "x" + str(size.height()) + ", Tamaño: " + str(file_info.size()))

    # Función para hacer zoom en las dos imágenes al mismo tiempo
    def wheelEvent(self, event):
        self.ndvi_view.wheelEvent(event)
        self.rgb_view.wheelEvent(event)

    # Método para habilitar la opción de selección
    def selectROI(self):
        self.ndvi_view.startSelectROI()

    def opencvFunc(self):
        area = self.ndvi_view._scene.sceneRect()

        #Obtener imagen de la escenea en QGraphicsView
        scene = QImage(area.width(), area.height(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(scene)

        self.ndvi_view._scene.render(painter, area)
        painter.end()
        
        scene = scene.convertToFormat(QtGui.QImage.Format.Format_RGB32)

        width = scene.width()
        height = scene.height()

        ptr = scene.bits()
        ptr.setsize(height * width * 4)

        # Escena convertida en imágen
        sceneImage = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))

        hsv = cv2.cvtColor(sceneImage, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        selection = cv2.inRange(hsv, lower_red, upper_red)

        h, w = selection.shape[:2]
        floodMask = np.zeros((h+2, w+2), np.uint8)

        cv2.floodFill(selection, floodMask, (0,0), 255)
        mask = cv2.bitwise_not(selection)

        pixels = cv2.bitwise_and(sceneImage, sceneImage, mask=mask)
        print(pixels)

        cv2.imshow('mask', mask)
        cv2.imshow('pixeles', pixels)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainNDVI()
    widget.show()
    sys.exit(app.exec_())
