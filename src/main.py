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

from PySide2 import QtWidgets, QtCore, QtSerialPort

from ui.confirm_send import Ui_confirmSend
from ui.loader import Ui_Loader
from ui.main import Ui_MainWindow
from ui.send_status import Ui_sendStatus


class Sender(QtCore.QThread):
    def __init__(self,
                 portname: str,
                 filepath: str,
                 parent: QtCore.QObject = None
                 ):
        super(Sender, self).__init__(parent)
        self.filepath = filepath
        self._size = int(0)
        self._size_sum = int(0)
        try:
            self.port = QtSerialPort.QSerialPort(portname, self)
            self.port.setBaudRate(self.port.Baud19200)
            self.port.setDataBits(self.port.Data7)
            self.port.setParity(self.port.EvenParity)
            self.port.setStopBits(self.port.TwoStop)
            self.port.setFlowControl(self.port.SoftwareControl)
        except QtSerialPort.QSerialPort.DeviceNotFoundError as e:
            raise ValueError(e)

    def run(self):
        self.port.open(self.port.ReadWrite)
        if not self.port.isOpen():
            print('Error %s' % self.port.error())
            print(self.port.errorString())
            return
        with open(self.filepath, 'r') as file:
            file.seek(0, 2)
            self._size = file.tell()
            file.seek(0, 0)
            self.port.write(QtCore.QByteArray('%'.encode('utf-8')))
            self.port.waitForBytesWritten()
            for line in file.readlines():
                self.port.write(QtCore.QByteArray(line.encode('UTF-8')))
                self.port.waitForBytesWritten()
                print(line, end='')
                self._size_sum += len(line) + 1
        self.port.write(QtCore.QByteArray('%'.encode('utf-8')))
        self.port.waitForBytesWritten()
        self.port.close()

    def getStatus(self) -> int:
        return self._size_sum * 100 // self._size


class SendStatus(QtWidgets.QDialog):
    def __init__(self,
                 parent: QtCore.QObject = None,
                 sender: Sender = None
                 ):
        super(SendStatus, self).__init__(parent)
        self.sender = sender
        self.ui = Ui_sendStatus()
        self.ui.setupUi(self)
        if self.sender is not None:
            self.timer_id = self.startTimer(500)
        else:
            self.ui.progressBar.setVisible(False)

    def update_status(self, status):
        self.ui.progressBar.setValue(status)
        if status == 100:
            self.ui.buttonBox.setEnabled(True)
            self.killTimer(self.timer_id)
        self.repaint()

    def timerEvent(self, event: QtCore.QTimerEvent):
        event.accept()
        self.update_status(self.sender.getStatus())


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
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            self.ui.serialPortChooser.addItem(port.portName())
        self.ui.serialPortChooser.setCurrentIndex(0)
        self.ui.serialPortChooser.currentTextChanged.connect(self.selection_changed)
        self.send_status = SendStatus
        self.sender = Sender
        self.sender = Sender

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
            filepath = self.dir.path() + '/' + filename
            port_chosen = self.ui.serialPortChooser.currentText()
            confirm = ConfirmSend(self)
            confirm.ui.dialogLabel.setText(f'Send program \'{filename}\'?')
            confirm.exec()
            if confirm.result() == confirm.Accepted:
                # Send program
                self.sender = Sender(port_chosen, filepath)
                self.send_status = SendStatus(self, self.sender)
                self.send_status.show()
                self.sender.start()
                self.send_status.exec_()


class SerialProgramLoader(QtWidgets.QMainWindow):
    def __init__(self):
        super(SerialProgramLoader, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loaderTabLayout.addWidget(Loader())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Serial Program Loader')
    app.setApplicationVersion('0.0.0')
    parser = QtCore.QCommandLineParser()
    parser.setApplicationDescription('Program to send Machining routines to '
                                     'CNC machines via serial port')
    startFullScreen = QtCore.QCommandLineOption(('f', 'fullscreen'), "Start in fullscreen mode")
    parser.addOption(startFullScreen)
    parser.addHelpOption()
    parser.addVersionOption()
    parser.process(app)
    window = SerialProgramLoader()
    if parser.isSet(startFullScreen):
        window.showFullScreen()
    else:
        window.show()
    ret = app.exec_()
    sys.exit(ret)
