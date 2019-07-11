# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\popup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 147)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spad_lbl = QtWidgets.QLabel(Dialog)
        self.spad_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.spad_lbl.setObjectName("spad_lbl")
        self.horizontalLayout_2.addWidget(self.spad_lbl)
        self.spad_txt = QtWidgets.QLineEdit(Dialog)
        self.spad_txt.setObjectName("spad_txt")
        self.horizontalLayout_2.addWidget(self.spad_txt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lab_lbl = QtWidgets.QLabel(Dialog)
        self.lab_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.lab_lbl.setObjectName("lab_lbl")
        self.horizontalLayout_4.addWidget(self.lab_lbl)
        self.lab_txt = QtWidgets.QLineEdit(Dialog)
        self.lab_txt.setObjectName("lab_txt")
        self.horizontalLayout_4.addWidget(self.lab_txt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.btnOptions = QtWidgets.QDialogButtonBox(Dialog)
        self.btnOptions.setOrientation(QtCore.Qt.Horizontal)
        self.btnOptions.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnOptions.setObjectName("btnOptions")
        self.verticalLayout.addWidget(self.btnOptions)

        self.retranslateUi(Dialog)
        self.btnOptions.accepted.connect(Dialog.accept)
        self.btnOptions.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ingresar Valores"))
        self.spad_lbl.setText(_translate("Dialog", "SPAD:"))
        self.lab_lbl.setText(_translate("Dialog", "LAB:"))

