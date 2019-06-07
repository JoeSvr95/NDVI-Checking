import sys
import numpy as np
import cv2

from views import ndvi_ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen

class MainNDVI(ndvi_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainNDVI, self).__init__()
        loadUi('views/ndvi_ui.ui', self)
        self.loadImgBtn.clicked.connect(self.setImage)
        self.lastPoint = QPoint()


    # Method to load image
    def setImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Cargar Imagen", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)
            self.drawing = False
            self.lastPoint = QPoint(self.imageLbl.pos())
            self.imageLbl.setPixmap(pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
            self.fileName = fileName

    def paintEvent(self, event):
        painter = QPainter(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.imageLbl.pixmap())
            painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.imageLbl.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainNDVI()
    widget.show()
    sys.exit(app.exec_())
