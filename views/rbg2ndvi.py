# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbg2ndvi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_rgb_visualizer(object):
    def setupUi(self, rgb_visualizer):
        rgb_visualizer.setObjectName("rgb_visualizer")
        rgb_visualizer.resize(779, 660)
        self.centralwidget = QtWidgets.QWidget(rgb_visualizer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.rgbview = RGBViewer(self.centralwidget)
        self.rgbview.setObjectName("rgbview")
        self.verticalLayout.addWidget(self.rgbview)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        rgb_visualizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rgb_visualizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        rgb_visualizer.setMenuBar(self.menubar)
        self.rgbinfo = QtWidgets.QStatusBar(rgb_visualizer)
        self.rgbinfo.setObjectName("rgbinfo")
        rgb_visualizer.setStatusBar(self.rgbinfo)
        self.actionAbrir_Imagen = QtWidgets.QAction(rgb_visualizer)
        self.actionAbrir_Imagen.setObjectName("actionAbrir_Imagen")
        self.actionCerrar = QtWidgets.QAction(rgb_visualizer)
        self.actionCerrar.setObjectName("actionCerrar")
        self.menuArchivo.addAction(self.actionAbrir_Imagen)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(rgb_visualizer)
        QtCore.QMetaObject.connectSlotsByName(rgb_visualizer)

    def retranslateUi(self, rgb_visualizer):
        _translate = QtCore.QCoreApplication.translate
        rgb_visualizer.setWindowTitle(_translate("rgb_visualizer", "Obtener NDVI"))
        self.label.setText(_translate("rgb_visualizer", "Valor RGB del pixel:"))
        self.label_3.setText(_translate("rgb_visualizer", "Valor NDVI del pixel:"))
        self.menuArchivo.setTitle(_translate("rgb_visualizer", "Archivo"))
        self.actionAbrir_Imagen.setText(_translate("rgb_visualizer", "Abrir Imagen"))
        self.actionCerrar.setText(_translate("rgb_visualizer", "Cerrar"))

from ndvi_lib.ndvi_class import RGBViewer
