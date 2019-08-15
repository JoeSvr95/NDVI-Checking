import sys
import numpy as np
import cv2

from views.rbg2chla import Ui_rgb_visualizer

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QFileInfo
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

class MainRGB2NDVI(Ui_rgb_visualizer, QMainWindow):
    def __init__(self):
        super(MainRGB2NDVI, self).__init__()
        self.setupUi(self)
        # Conectando acciones del menú
        self.actionAbrir_Imagen.triggered.connect(self.loadRGBImage)
    
    # Método para cargar una imágen a un widget y colocar información
    def loadImage(self, widget, info):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)")
        image = QFileInfo(fileName).fileName()
        if fileName:
            pixmap = QPixmap(fileName)
            file_size = QFileInfo(fileName).size()
            size = pixmap.size()
            widget.RGBImage = cv2.imread(fileName)
            widget.setImage(pixmap)
            info.showMessage("Resolución: " + str(size.width()) + "x" + str(size.height()) + ", Tamaño: " + format_bytes(file_size))
        return image

    # Método para colocar una imagen en el widget de RGB
    def loadRGBImage(self):
        self.loadImage(self.rgbview, self.rgbinfo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainRGB2NDVI()
    widget.show()
    sys.exit(app.exec_())
