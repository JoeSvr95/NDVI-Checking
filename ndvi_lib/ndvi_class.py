from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QPen

class ImageViewer(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(ImageViewer, self).__init__(parent)
        # Instance variables for basic image control
        self.zoom = 0
        self.empty = True
        self.image = QtWidgets.QGraphicsPixmapItem()
        self._scene = QtWidgets.QGraphicsScene(self)
        self._scene.addItem(self.image)
        self.setScene(self._scene)
        # Instance variables for selection
        self.firstPoint = QPoint()
        self.lastPoint = QPoint()
        self.select = False
        self.drawing = False

    def fitInView(self):
        rect = QtCore.QRectF(self.image.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasImage():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1/unity.width(), 1/unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width()/scenerect.width(),
                             viewrect.height()/scenerect.height())
                self.scale(factor, factor)
        self.zoom = 0

    def hasImage(self):
        return not self.empty

    def setImage(self, pixmap=None):
        self.zoom = 0
        if pixmap and not pixmap.isNull():
            self.empty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self.image.setPixmap(pixmap)
        else:
            self.empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self.image.setPixmap(QtGui.QPixmap)

    def wheelEvent(self, event):
        if self.hasImage():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self.zoom += 1
            else:
                factor = 0.8
                self.zoom -= 1
            if self.zoom > 0:
                self.scale(factor, factor)
            elif self.zoom == 0:
                self.fitInView()
            else:
                self.zoom = 0
    '''    
    # Crea el objeto painter e inicia bandera para seleccionar
    def startSelectROI(self):
        self.setCursor(Qt.CrossCursor)
        self.select = True

    # Al hacer click se empieza a dibujar
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.select:
            self.drawing = True
            self.lastPoint = event.pos()
            self.firstPoint = event.pos()

    # Al mover el mouse se dibuja el paso del mouse
    def mouseMoveEvent(self, event):
        if event.button() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.viewport.pixmap())
            painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.image.update()

    # Si el usuario no ha completado una figura cerrada
    # Esta función completa la figura
    def mouseReleaseEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image.pixmap())
            painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))
            painter.drawLine(self.firstPoint, self.lastPoint)
            self.drawing = False
            self.image.update()
    '''