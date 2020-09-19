# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'send_status.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sendStatus(object):
    def setupUi(self, sendStatus):
        if not sendStatus.objectName():
            sendStatus.setObjectName(u"sendStatus")
        sendStatus.resize(250, 110)
        sendStatus.setMinimumSize(QSize(250, 110))
        self.verticalLayout = QVBoxLayout(sendStatus)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(sendStatus)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(sendStatus)
        self.progressBar.setObjectName(u"progressBar")

        self.verticalLayout.addWidget(self.progressBar)

        self.buttonBox = QDialogButtonBox(sendStatus)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(sendStatus)
        self.buttonBox.clicked.connect(sendStatus.close)

        QMetaObject.connectSlotsByName(sendStatus)
    # setupUi

    def retranslateUi(self, sendStatus):
        sendStatus.setWindowTitle(QCoreApplication.translate("sendStatus", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("sendStatus", u"TextLabel", None))
    # retranslateUi

