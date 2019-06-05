import sys
import numpy as np
import cv2

from views import ndvi_ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap

class MainNDVI(ndvi_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainNDVI, self).__init__()
        loadUi('views/ndvi_ui.ui', self)
        self.loadImgBtn.clicked.connect(self.setImage)

    # Method to load image
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            image = cv2.imread(fileName)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            step = channel * width
            # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            self.imageLbl.setPixmap(QPixmap.fromImage(qImg))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainNDVI()
    widget.show()
    sys.exit(app.exec_())
