# MIT License
#
# Copyright (c) 2020 Simão Amorim <simao_amorim@outlook.pt>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

from PyQt5 import QtWidgets, QtCore

from ui.loader import Ui_Loader
from ui.main import Ui_MainWindow


class Loader(QtWidgets.QWidget):
    def __init__(self):
        super(Loader, self).__init__()
        self.ui = Ui_Loader()
        self.ui.setupUi(self)
        self.path = QtCore.QDir.currentPath()
        self.filter = QtCore.QDir
        self.fsmodel = QtWidgets.QFileSystemModel()
        self.fsmodel.setFilter(QtCore.QDir.Files)
        self.ui.programListView.setModel(self.fsmodel)
        self.fsmodel.setRootPath(self.path)
        self.ui.programListView.setRootIndex(
            self.fsmodel.index(self.path)
        )


class SerialProgramLoader(QtWidgets.QMainWindow):
    def __init__(self):
        super(SerialProgramLoader, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loaderTabLayout.addWidget(Loader())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SerialProgramLoader()
    window.show()
    # window.showFullScreen()
    ret = app.exec()
    sys.exit(ret)
