# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ndvi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 828)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tools_frame = QtWidgets.QFrame(self.main_frame)
        self.tools_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tools_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools_frame.setObjectName("tools_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tools_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loadImgBtn = QtWidgets.QPushButton(self.tools_frame)
        self.loadImgBtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadImgBtn.sizePolicy().hasHeightForWidth())
        self.loadImgBtn.setSizePolicy(sizePolicy)
        self.loadImgBtn.setObjectName("loadImgBtn")
        self.horizontalLayout_3.addWidget(self.loadImgBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.tools_frame)
        self.img_frame = QtWidgets.QFrame(self.main_frame)
        self.img_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img_frame.setObjectName("img_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.img_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.img_frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1030, 678))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.horizontalLayout.addWidget(self.imageLbl)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.img_frame)
        self.gridLayout_2.addWidget(self.main_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NDVI Labeling"))
        self.loadImgBtn.setText(_translate("MainWindow", "Cargar Imagen"))

