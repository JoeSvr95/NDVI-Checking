# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbg2chla.ui'
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
        self.lblRGB = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRGB.sizePolicy().hasHeightForWidth())
        self.lblRGB.setSizePolicy(sizePolicy)
        self.lblRGB.setObjectName("lblRGB")
        self.horizontalLayout_2.addWidget(self.lblRGB)
        self.lblRGBValue = QtWidgets.QLabel(self.centralwidget)
        self.lblRGBValue.setText("")
        self.lblRGBValue.setObjectName("lblRGBValue")
        self.horizontalLayout_2.addWidget(self.lblRGBValue)
        self.lblCHLA = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCHLA.sizePolicy().hasHeightForWidth())
        self.lblCHLA.setSizePolicy(sizePolicy)
        self.lblCHLA.setObjectName("lblCHLA")
        self.horizontalLayout_2.addWidget(self.lblCHLA)
        self.lblCHLAValue = QtWidgets.QLabel(self.centralwidget)
        self.lblCHLAValue.setText("")
        self.lblCHLAValue.setObjectName("lblCHLAValue")
        self.horizontalLayout_2.addWidget(self.lblCHLAValue)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.rgbview = RGB2CHLA(self.centralwidget)
        self.rgbview.setObjectName("rgbview")
        self.verticalLayout.addWidget(self.rgbview)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        rgb_visualizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rgb_visualizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 26))
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
        rgb_visualizer.setWindowTitle(_translate("rgb_visualizer", "Obtener Clorofila"))
        self.lblRGB.setText(_translate("rgb_visualizer", "Valor NDVI del pixel:"))
        self.lblCHLA.setText(_translate("rgb_visualizer", "Valor de clorofilal:"))
        self.menuArchivo.setTitle(_translate("rgb_visualizer", "Archivo"))
        self.actionAbrir_Imagen.setText(_translate("rgb_visualizer", "Abrir Imagen"))
        self.actionCerrar.setText(_translate("rgb_visualizer", "Cerrar"))

from ndvi_lib.ndvi_class import RGB2CHLA
