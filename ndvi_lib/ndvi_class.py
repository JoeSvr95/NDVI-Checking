from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, Qt, QLineF, pyqtSlot
from PyQt5.QtGui import QPainterPath, QPen, QPainter, QImage, QPixmap, QIntValidator
from PyQt5.QtWidgets import QMessageBox, QGraphicsTextItem

from views.popup_ui import Ui_Dialog

import services.data_services as svc

'''
    Clase que hereda de QGraphicsView
    Utilizada para mostar imagenes RGB y poder hacer manipulaciones básicas
    Agregar imagen, zoom, drag
'''
class RGBViewer(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(RGBViewer, self).__init__(parent)
        # Variables de instancia para manipulación básica
        self.zoom = 0
        self.empty = True
        self.image = QtWidgets.QGraphicsPixmapItem()
        self._scene = QtWidgets.QGraphicsScene(self)
        self._scene.addItem(self.image)
        self.setScene(self._scene)

    # Mostrar imagen completa dentro del widget
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

    # Retorna verdadero o false dependiendo si el widget tiene una imagen
    def hasImage(self):
        return not self.empty

    # Agregar una imagen al widget
    def setImage(self, pixmap=None):
        self.zoom = 0
        # Si tiene una imagen se puede arrastrar la imagen
        if pixmap and not pixmap.isNull():
            self.empty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self.image.setPixmap(pixmap)
        # Si no tiene imagen se deshabilita la opción de arrastrar
        else:
            self.empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self.image.setPixmap(QtGui.QPixmap)

    # Hacer zoom en el evento en que se mueva la rueda del mouse
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
    Clase que hereda de RGBViewer
    Se usa para poder dibujar encima de la imagen y mantener las mismas
    acciones básicas de manipulación
'''
class NDVIViewer(RGBViewer):
    start = None # Inicio de la línea
    end = None # Fin de la línea
    item = None
    path = None
    ndvi_filename = None

    def __init__(self, parent):
        super(NDVIViewer, self).__init__(parent)
        self.path = QPainterPath()
        self.item = GraphicPathItem()
        self.scene().addItem(self.item)
        self.select = False
        self.drawing = False
        self.ui = ValuesDialog(self)

    # Función para poder validar si se puede dibujar o no
    def startSelectROI(self):
        if self.select:
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag) # Se habilita el arrastre de la imagen
            self.setCursor(Qt.OpenHandCursor) # Se pone de cursos una mano
            self.select = False
        else:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag) # Se deshabilita el arrastre para dibujar
            self.setCursor(Qt.CrossCursor) # Se pone de cursor una cruz
            self.select = True

    # Se inicia bandera para poder dibujar
    def mousePressEvent(self, event):
        if self.select:
            self.drawing = True
            self.start = self.mapToScene(event.pos())
            self.path.moveTo(self.start)
        else:
            super(NDVIViewer, self).mousePressEvent(event)

    # Función para dibujar
    def mouseMoveEvent(self, event):
        if self.select and self.drawing:
            self.end = self.mapToScene(event.pos())
            self.path.lineTo(self.end)
            self.item.setPath(self.path)
        else:
            super(NDVIViewer, self).mouseMoveEvent(event)

    # Se completa el dibujo para una figura cerrada
    def mouseReleaseEvent(self, event):
        if self.select:
            self.path.lineTo(self.start)
            self.item.setPath(self.path)
            self.start = False
            self.drawing = False
            self.select = False
            self.ui.filename = self.ndvi_filename
            self.ui.exec_()
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag) 
            self.setCursor(Qt.OpenHandCursor)
        else:
            super(NDVIViewer, self).mouseReleaseEvent(event)

    def deleteLastSelection(self):
        self._scene.removeItem(self.item)
        self.path = QPainterPath()
        self.item = GraphicPathItem()
        self.scene().addItem(self.item)

# Clase para definir el color de la selección
class GraphicPathItem(QtWidgets.QGraphicsPathItem):
    def __init__(self):
        super(GraphicPathItem, self).__init__()
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(5)
        self.setPen(pen)

# Clase del pop-up para ingresar valores
class ValuesDialog(QtWidgets.QDialog, Ui_Dialog):
    filename = None

    def __init__(self, parent):
        super(ValuesDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.validator = QIntValidator()
        self.spad_txt.setValidator(self.validator)
        self.lab_txt.setValidator(self.validator)

    @pyqtSlot()
    def accept(self):
        spad_text = self.spad_txt.text()
        lab_text = self.lab_txt.text()

        if spad_text and lab_text:
            # Guardando datos
            spad = float(spad_text)
            lab = float(lab_text)
            svc.create_ndvi(self.filename ,spad, lab)
            QMessageBox.information(self, "Información", "Los datos se han guardado exitosamente", QMessageBox.Ok)
            # Añadiendo label en la selección
            pos = self.parent.end
            self.addLabel(self.spad_lbl.text(), spad_text, pos)
            pos.setY(pos.y() + 20)
            self.addLabel(self.lab_lbl.text(), lab_text, pos) 
        else:
            QMessageBox.warning(self, "Error", "No se pudo ingresar los datos", QMessageBox.Ok)
            
        self.spad_txt.clear()
        self.lab_txt.clear()
        self.done(QtWidgets.QDialog.Accepted)

    @pyqtSlot()
    def reject(self):
        self.parent.deleteLastSelection()
        self.done(QtWidgets.QDialog.Rejected)

    def addLabel(self, valueType, value, position):
        label = QGraphicsTextItem()
        label.setPlainText(valueType + value)
        label.setPos(position)
        self.parent.scene().addItem(label)
    

