# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loader(object):
    def setupUi(self, Loader):
        Loader.setObjectName("Loader")
        Loader.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(Loader)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Loader)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Loader)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.programListView = QtWidgets.QListView(Loader)
        self.programListView.setObjectName("programListView")
        self.gridLayout_2.addWidget(self.programListView, 1, 0, 1, 1)

        self.retranslateUi(Loader)
        QtCore.QMetaObject.connectSlotsByName(Loader)

    def retranslateUi(self, Loader):
        _translate = QtCore.QCoreApplication.translate
        Loader.setWindowTitle(_translate("Loader", "Form"))
        self.label.setText(_translate("Loader", "TextLabel"))
        self.pushButton.setText(_translate("Loader", "PushButton"))