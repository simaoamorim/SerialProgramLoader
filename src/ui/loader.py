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
        Loader.resize(480, 230)
        font = QFont()
        font.setPointSize(12)
        Loader.setFont(font)
        Loader.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.gridLayout = QGridLayout(Loader)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.programListWidget = QListWidget(Loader)
        self.programListWidget.setObjectName(u"programListWidget")
        self.programListWidget.setAlternatingRowColors(True)
        self.programListWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.programListWidget.setUniformItemSizes(True)
        self.programListWidget.setWordWrap(True)
        self.programListWidget.setSelectionRectVisible(True)

        self.gridLayout.addWidget(self.programListWidget, 0, 0, 1, 1)

        self.frame = QFrame(Loader)
        self.frame.setObjectName(u"frame")
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.updateProgramListButton = QPushButton(self.frame)
        self.updateProgramListButton.setObjectName(u"updateProgramListButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateProgramListButton.sizePolicy().hasHeightForWidth())
        self.updateProgramListButton.setSizePolicy(sizePolicy)
        self.updateProgramListButton.setMinimumSize(QSize(0, 35))

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.updateProgramListButton)

        self.port_label = QLabel(self.frame)
        self.port_label.setObjectName(u"port_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.port_label)

        self.serialPortChooser = QComboBox(self.frame)
        self.serialPortChooser.setObjectName(u"serialPortChooser")
        self.serialPortChooser.setMinimumSize(QSize(0, 35))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.serialPortChooser)

        self.sendButton = QPushButton(self.frame)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.sendButton)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Loader)

        QMetaObject.connectSlotsByName(Loader)
    # setupUi

    def retranslateUi(self, Loader):
        Loader.setWindowTitle(QCoreApplication.translate("Loader", u"Form", None))
        self.updateProgramListButton.setText(QCoreApplication.translate("Loader", u"Refresh", None))
        self.port_label.setText(QCoreApplication.translate("Loader", u"Serial Port:", None))
        self.sendButton.setText(QCoreApplication.translate("Loader", u"Send", None))
    # retranslateUi

