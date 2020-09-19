# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_send.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_confirmSend(object):
    def setupUi(self, confirmSend):
        if not confirmSend.objectName():
            confirmSend.setObjectName(u"confirmSend")
        confirmSend.resize(237, 110)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confirmSend.sizePolicy().hasHeightForWidth())
        confirmSend.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(confirmSend)
        self.verticalLayout.setSpacing(22)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(22, 22, 22, 22)
        self.dialogLabel = QLabel(confirmSend)
        self.dialogLabel.setObjectName(u"dialogLabel")

        self.verticalLayout.addWidget(self.dialogLabel)

        self.buttonBox = QDialogButtonBox(confirmSend)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(confirmSend)
        self.buttonBox.accepted.connect(confirmSend.accept)
        self.buttonBox.rejected.connect(confirmSend.reject)

        QMetaObject.connectSlotsByName(confirmSend)
    # setupUi

    def retranslateUi(self, confirmSend):
        confirmSend.setWindowTitle(QCoreApplication.translate("confirmSend", u"Dialog", None))
        self.dialogLabel.setText(QCoreApplication.translate("confirmSend", u"TextLabel", None))
    # retranslateUi

