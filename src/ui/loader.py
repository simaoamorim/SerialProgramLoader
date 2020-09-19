# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loader.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Loader(object):
    def setupUi(self, Loader):
        if not Loader.objectName():
            Loader.setObjectName(u"Loader")
        Loader.resize(400, 300)
        font = QFont()
        font.setPointSize(8)
        Loader.setFont(font)
        self.gridLayout_2 = QGridLayout(Loader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Loader)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.serialPortChooser = QComboBox(Loader)
        self.serialPortChooser.setObjectName(u"serialPortChooser")

        self.verticalLayout.addWidget(self.serialPortChooser)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.sendButton = QPushButton(Loader)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setEnabled(False)

        self.verticalLayout.addWidget(self.sendButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.programListWidget = QListWidget(Loader)
        self.programListWidget.setObjectName(u"programListWidget")
        self.programListWidget.setSelectionRectVisible(True)

        self.gridLayout_2.addWidget(self.programListWidget, 1, 0, 1, 1)

        self.updateProgramListButton = QPushButton(Loader)
        self.updateProgramListButton.setObjectName(u"updateProgramListButton")

        self.gridLayout_2.addWidget(self.updateProgramListButton, 0, 2, 1, 1)


        self.retranslateUi(Loader)

        QMetaObject.connectSlotsByName(Loader)
    # setupUi

    def retranslateUi(self, Loader):
        Loader.setWindowTitle(QCoreApplication.translate("Loader", u"Form", None))
        self.label.setText(QCoreApplication.translate("Loader", u"TextLabel", None))
        self.sendButton.setText(QCoreApplication.translate("Loader", u"Send", None))
        self.updateProgramListButton.setText(QCoreApplication.translate("Loader", u"Refresh", None))
    # retranslateUi

