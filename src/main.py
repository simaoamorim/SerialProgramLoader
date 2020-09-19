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
import threading

from PySide2 import QtWidgets, QtCore, QtSerialPort, QtGui

from ui.loader import Ui_Loader
from ui.main import Ui_MainWindow
from ui.confirm_send import Ui_confirmSend
from ui.send_status import Ui_sendStatus


class SendStatus(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SendStatus, self).__init__(parent)
        self.ui = Ui_sendStatus()
        self.ui.setupUi(self)

    def update_status(self, status):
        self.ui.progressBar.setValue(status)
        if status == 100:
            self.ui.buttonBox.setEnabled(True)
        self.update()


class ConfirmSend(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ConfirmSend, self).__init__(parent)
        self.ui = Ui_confirmSend()
        self.ui.setupUi(self)


class Loader(QtWidgets.QWidget):
    def __init__(self):
        super(Loader, self).__init__()
        self.ui = Ui_Loader()
        self.ui.setupUi(self)
        self.dir = QtCore.QDir(QtCore.QDir.currentPath()+'/programs/')
        print(self.dir.path())
        self.dir.setFilter(QtCore.QDir.Files or QtCore.QDir.NoDotAndDotDot)
        self.fs_watcher = QtCore.QFileSystemWatcher(self.dir.path())
        self.fs_watcher.addPath(self.dir.path())
        # self.connect(
        #     self.fs_watcher,
        #     QtCore.SIGNAL('directoryChanged()'),
        #     self,
        #     QtCore.SLOT('update_program_list()')
        # )
        self.ui.updateProgramListButton.clicked.connect(self.update_program_list)
        self.ui.programListWidget.itemSelectionChanged.connect(self.selection_changed)
        self.ui.sendButton.clicked.connect(self.send_program)
        self.update_program_list()
        ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for port in ports:
            self.ui.serialPortChooser.addItem(port.portName())
        self.ui.serialPortChooser.setCurrentIndex(0)
        self.ui.serialPortChooser.currentTextChanged.connect(self.selection_changed)
        self.send_status = SendStatus

    def update_program_list(self):
        self.ui.programListWidget.clear()
        self.dir.refresh()
        self.ui.programListWidget.addItems(
            self.dir.entryList()
        )
        self.ui.programListWidget.clearSelection()
        self.ui.sendButton.setDisabled(True)

    def selection_changed(self):
        if self.ui.serialPortChooser.currentText() != '' and self.ui.programListWidget.currentItem() is not None:
            self.ui.sendButton.setEnabled(True)

    def send_program(self):
        selections = self.ui.programListWidget.selectedItems()
        for selection in selections:
            filename = selection.text()
            filepath = self.dir.path() + '/' + selection.text()
            port_chosen = self.ui.serialPortChooser.currentText()
            port_info = QtSerialPort.QSerialPortInfo(port_chosen)
            confirm = ConfirmSend(self)
            confirm.ui.dialogLabel.setText(f'Send program \'{filename}\'?')
            confirm.exec()
            if confirm.result() == confirm.Accepted:
                # Send program
                self.send_status = SendStatus(self)
                self.send_status.show()
                port = QtSerialPort.QSerialPort(port_info, self)
                print('Setting port baud...', end='')
                port.setBaudRate(port.Baud19200)
                print('done')
                print('Opening port...', end='')
                port.open(
                    port.ReadWrite |
                    port.NoFlowControl |
                    port.EvenParity |
                    port.TwoStop |
                    port.Data7
                )
                if not port.isOpen():
                    print('Error %' % port.error())
                    print(port.errorString())
                    return
                print('done')
                port.write(QtCore.QByteArray('%'.encode('utf-8')))
                port.waitForBytesWritten()
                with open(filepath, 'r') as file:
                    file.seek(0, 2)
                    _size = file.tell()
                    file.seek(0, 0)
                    _size_sum = 0
                    for line in file.readlines():
                        port.write(QtCore.QByteArray(line.encode('UTF-8')))
                        port.waitForBytesWritten()
                        # port.flush()
                        print(line, end='')
                        _size_sum += len(line) + 1
                        if self.send_status is not None:
                            self.send_status.update_status(int(min(_size_sum * 100 // _size, 100)))
                port.write(QtCore.QByteArray('%'.encode('utf-8')))
                port.waitForBytesWritten()
                port.close()
                self.send_status.exec_()
                # thread.join()
                print('ok')
            else:
                print('Nothing done')


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
    ret = app.exec_()
    sys.exit(ret)
