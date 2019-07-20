import sys
import numpy as np
import cv2
import data.mongo_setup as mongo_setup

from views.ndvi_ui import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QPoint, Qt, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap

# Convierte el número de bytes en formato más legible
def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'KB', 2: 'MB', 3: 'GB'}
    while size > power:
        size /= power
        n += 1
    return '%.2f%s' % (size, power_labels[n])

class MainNDVI(Ui_MainWindow, QMainWindow):
    def __init__(self): # Inicializa todos los atributos y los widgets
        super(MainNDVI, self).__init__()
        self.setupUi(self)
        self.loadRGBBtn.clicked.connect(self.loadRGBImage)
        self.loadNDVIBtn.clicked.connect(self.loadNDVIImage)
        self.selectBtn.clicked.connect(self.selectROI)
        mongo_setup.global_init()

    # Método para colocar una imagen en el widget de RGB
    def loadRGBImage(self):
        self.loadImage(self.rgb_view, self.rgb_info)
    
    # Método para colocar una imagen en el widget de NDVI
    def loadNDVIImage(self):
        ndvi_image = self.loadImage(self.ndvi_view, self.ndvi_info)
        self.ndvi_view.ndvi_filename = ndvi_image
        self.selectBtn.setEnabled(True)

    # Método para cargar una imágen a un widget y colocar información
    def loadImage(self, widget, info):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        image = QFileInfo(fileName).fileName()
        if fileName:
            pixmap = QPixmap(fileName)
            file_size = QFileInfo(fileName).size()
            size = pixmap.size()
            widget.setImage(pixmap)
            info.setText("Resolución: " + str(size.width()) + "x" + str(size.height()) + ", Tamaño: " + format_bytes(file_size))
        return image

    # Función para hacer zoom en las dos imágenes al mismo tiempo
    def wheelEvent(self, event):
        self.ndvi_view.wheelEvent(event)
        self.rgb_view.wheelEvent(event)

    def selectROI(self):
        self.selectBtn.setDown(True)
        self.ndvi_view.startSelectROI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainNDVI()
    widget.show()
    sys.exit(app.exec_())
