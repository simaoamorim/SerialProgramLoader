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
        Loader.resize(483, 384)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Loader.sizePolicy().hasHeightForWidth())
        Loader.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        Loader.setFont(font)
        Loader.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.gridLayout = QGridLayout(Loader)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.programListWidget = QListWidget(Loader)
        self.programListWidget.setObjectName(u"programListWidget")

        self.gridLayout.addWidget(self.programListWidget, 0, 0, 1, 1)

        self.frame = QFrame(Loader)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.updateProgramListButton = QPushButton(self.frame)
        self.updateProgramListButton.setObjectName(u"updateProgramListButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.updateProgramListButton.sizePolicy().hasHeightForWidth())
        self.updateProgramListButton.setSizePolicy(sizePolicy1)
        self.updateProgramListButton.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.updateProgramListButton)

        self.port_label = QLabel(self.frame)
        self.port_label.setObjectName(u"port_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.port_label)

        self.serialPortChooser = QComboBox(self.frame)
        self.serialPortChooser.setObjectName(u"serialPortChooser")
        self.serialPortChooser.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.serialPortChooser)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.groupBox.setCheckable(False)
        self.serialPortConfigurationBox = QFormLayout(self.groupBox)
        self.serialPortConfigurationBox.setObjectName(u"serialPortConfigurationBox")
        self.serialPortConfigurationBox.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.serialPortConfigurationBox.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.baudrate_label = QLabel(self.groupBox)
        self.baudrate_label.setObjectName(u"baudrate_label")
        self.baudrate_label.setScaledContents(False)

        self.serialPortConfigurationBox.setWidget(0, QFormLayout.LabelRole, self.baudrate_label)

        self.parity_label = QLabel(self.groupBox)
        self.parity_label.setObjectName(u"parity_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.parity_label.sizePolicy().hasHeightForWidth())
        self.parity_label.setSizePolicy(sizePolicy3)

        self.serialPortConfigurationBox.setWidget(1, QFormLayout.LabelRole, self.parity_label)

        self.parityChooser = QComboBox(self.groupBox)
        self.parityChooser.setObjectName(u"parityChooser")
        self.parityChooser.setMinimumSize(QSize(0, 30))

        self.serialPortConfigurationBox.setWidget(1, QFormLayout.FieldRole, self.parityChooser)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)

        self.serialPortConfigurationBox.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.dataBitsChooser = QComboBox(self.groupBox)
        self.dataBitsChooser.setObjectName(u"dataBitsChooser")
        self.dataBitsChooser.setMinimumSize(QSize(0, 30))

        self.serialPortConfigurationBox.setWidget(2, QFormLayout.FieldRole, self.dataBitsChooser)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setScaledContents(False)

        self.serialPortConfigurationBox.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.stopBitsChooser = QComboBox(self.groupBox)
        self.stopBitsChooser.setObjectName(u"stopBitsChooser")
        self.stopBitsChooser.setMinimumSize(QSize(0, 30))

        self.serialPortConfigurationBox.setWidget(3, QFormLayout.FieldRole, self.stopBitsChooser)

        self.flowControlChooser = QComboBox(self.groupBox)
        self.flowControlChooser.setObjectName(u"flowControlChooser")
        self.flowControlChooser.setMinimumSize(QSize(0, 30))

        self.serialPortConfigurationBox.setWidget(4, QFormLayout.FieldRole, self.flowControlChooser)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.serialPortConfigurationBox.setWidget(4, QFormLayout.LabelRole, self.label)

        self.baudRateInput = QLineEdit(self.groupBox)
        self.baudRateInput.setObjectName(u"baudRateInput")
        self.baudRateInput.setMinimumSize(QSize(0, 30))

        self.serialPortConfigurationBox.setWidget(0, QFormLayout.FieldRole, self.baudRateInput)


        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.groupBox)

        self.sendButton = QPushButton(self.frame)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.sendButton)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 300)

        self.retranslateUi(Loader)

        QMetaObject.connectSlotsByName(Loader)
    # setupUi

    def retranslateUi(self, Loader):
        Loader.setWindowTitle(QCoreApplication.translate("Loader", u"Form", None))
        self.updateProgramListButton.setText(QCoreApplication.translate("Loader", u"Refresh", None))
        self.port_label.setText(QCoreApplication.translate("Loader", u"Serial Port:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Loader", u"Serial Port configuration", None))
        self.baudrate_label.setText(QCoreApplication.translate("Loader", u"Baudrate:", None))
        self.parity_label.setText(QCoreApplication.translate("Loader", u"Parity:", None))
        self.label_2.setText(QCoreApplication.translate("Loader", u"Data Bits:", None))
        self.label_3.setText(QCoreApplication.translate("Loader", u"Stop Bits:", None))
        self.label.setText(QCoreApplication.translate("Loader", u"Flow Control:", None))
        self.sendButton.setText(QCoreApplication.translate("Loader", u"Send", None))
    # retranslateUi

