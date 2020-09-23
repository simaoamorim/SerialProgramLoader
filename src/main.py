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

from PySide2.QtCore import QByteArray, QDir, QFileSystemWatcher, QThread, \
    QObject, QSettings, QCommandLineOption, QCommandLineParser, QTimerEvent, \
    QBasicMutex
from PySide2.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide2.QtWidgets import QMessageBox, QApplication, QVBoxLayout, \
    QMainWindow, QDialog, QWidget

from ui.confirm_send import Ui_confirmSend
from ui.loader import Ui_Loader
from ui.main import Ui_MainWindow
from ui.send_status import Ui_sendStatus


def save_port(port: str):
    globalSettings.setValue('serialport/port', port)


def save_baud(baud: str):
    globalSettings.setValue('serialport/baudrate', baud)


def save_parity(parity: str):
    globalSettings.setValue('serialport/parity', parity)


def save_databits(databits: str):
    globalSettings.setValue('serialport/databits', databits)


def save_stopbits(stopbits: str):
    globalSettings.setValue('serialport/stopbits', stopbits)


def save_flowcontrol(flowcontrol: str):
    globalSettings.setValue('serialport/flowcontrol', flowcontrol)


class Sender(QThread):
    def __init__(self,
                 portname: str,
                 filepath: str,
                 baudrate: str,
                 databits: str,
                 parity: str,
                 stopbits: str,
                 flowcontrol: str,
                 parent: QObject = None
                 ):
        super(Sender, self).__init__(parent)
        self.filepath = filepath
        self.baudrate = QSerialPort.BaudRate.values.get(baudrate)
        self.databits = QSerialPort.DataBits.values.get(databits)
        self.parity = QSerialPort.Parity.values.get(parity)
        self.stopbits = QSerialPort.StopBits.values.get(stopbits)
        self.flowcontrol = QSerialPort.FlowControl.values.get(flowcontrol)
        with open(self.filepath, 'r') as file:
            file.seek(0, 2)
            self._size = file.tell()
            file.seek(0, 0)
        self._size_sum = int(0)
        self.mutex = QBasicMutex()
        try:
            self.port = QSerialPort(portname, self)
            self.port.setBaudRate(self.baudrate)
            self.port.setDataBits(self.databits)
            self.port.setParity(self.parity)
            self.port.setStopBits(self.stopbits)
            self.port.setFlowControl(self.flowcontrol)
        except QSerialPort.DeviceNotFoundError as e:
            raise ValueError(e)

    def run(self):
        self.port.open(self.port.ReadWrite)
        if not self.port.isOpen():
            print('Error %s' % self.port.error())
            print(self.port.errorString())
            return
        with open(self.filepath, 'r') as file:
            self.port.write(QByteArray('%'.encode('utf-8')))
            self.port.waitForBytesWritten()
            for line in file.readlines():
                self.port.write(QByteArray(line.encode('UTF-8')))
                self.port.waitForBytesWritten()
                print(line, end='')
                self.mutex.lock()
                self._size_sum += len(line) + 1
                self.mutex.unlock()
            self.port.write(QByteArray('%'.encode('utf-8')))
            self.port.waitForBytesWritten()
        self.port.close()

    def get_status(self) -> int:
        self.mutex.lock()
        try:
            tmp = self._size_sum * 100 // self._size
        except ZeroDivisionError:
            tmp = 0
        self.mutex.unlock()
        return tmp


class SendStatus(QDialog):
    def __init__(self,
                 parent: QObject = None,
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
        self.update()

    def timerEvent(self, event: QTimerEvent):
        event.accept()
        self.update_status(self.sender.get_status())
        if self.sender.isFinished() and self.ui.progressBar.value() != 100:
            self.killTimer(self.timer_id)
            QMessageBox.critical(
                self,
                'Error',
                self.sender.port.errorString()
            )
            self.close()


class ConfirmSend(QDialog):
    def __init__(self, parent=None):
        super(ConfirmSend, self).__init__(parent)
        self.ui = Ui_confirmSend()
        self.ui.setupUi(self)


class Loader(QWidget):
    def __init__(self, parent=None):
        super(Loader, self).__init__(parent=parent)
        self.ui = Ui_Loader()
        self.ui.setupUi(self)
        self.dir = QDir(QDir.currentPath() + '/programs/')
        self.dir.setFilter(QDir.Files or QDir.NoDotAndDotDot)
        self.fs_watcher = QFileSystemWatcher(self.dir.path())
        self.fs_watcher.addPath(self.dir.path())
        self.fs_watcher.directoryChanged.connect(self.update_program_list)
        self.send_status = SendStatus
        self.sender = Sender
        self.serialproperties = \
            {
                'baudrate': QSerialPort.BaudRate,
                'parity': QSerialPort.Parity,
                'databits': QSerialPort.DataBits,
                'stopbits': QSerialPort.StopBits,
                'flowcontrol': QSerialPort.FlowControl
            }
        self.serialpropertiesvalues = {}
        for (key, val) in self.serialproperties.items():
            self.serialpropertiesvalues[key] = \
                (
                    value for value in val.values.keys()
                    if not value.startswith('Unknown')
                )

        self.update_program_list()
        self.update_serial_port_list()
        self.set_serial_port_options()

        self.ui.updateProgramListButton.clicked.connect(self.refresh)
        self.ui.programListWidget.itemSelectionChanged.connect(
            self.selection_changed)
        self.ui.sendButton.clicked.connect(self.send_program)
        self.ui.serialPortChooser.currentTextChanged.connect(
            self.selection_changed)
        self.ui.serialPortChooser.currentTextChanged.connect(save_port)
        self.ui.baudrateChooser.currentTextChanged.connect(save_baud)
        self.ui.parityChooser.currentTextChanged.connect(save_parity)
        self.ui.dataBitsChooser.currentTextChanged.connect(save_databits)
        self.ui.stopBitsChooser.currentTextChanged.connect(save_stopbits)
        self.ui.flowControlChooser.currentTextChanged.connect(save_flowcontrol)

    def set_serial_port_options(self):
        self.ui.baudrateChooser.addItems(
            self.serialpropertiesvalues.get('baudrate')
        )
        self.ui.parityChooser.addItems(
            self.serialpropertiesvalues.get('parity')
        )
        self.ui.dataBitsChooser.addItems(
            self.serialpropertiesvalues.get('databits')
        )
        self.ui.stopBitsChooser.addItems(
            self.serialpropertiesvalues.get('stopbits')
        )
        self.ui.flowControlChooser.addItems(
            self.serialpropertiesvalues.get('flowcontrol')
        )
        if globalSettings.contains('serialport/port'):
            self.selectpreviousvalues()
        else:
            self.saveconfig()

    def selectpreviousvalues(self):
        self.ui.serialPortChooser.setCurrentText(
            globalSettings.value('serialport/port')
        )
        self.ui.baudrateChooser.setCurrentText(
            globalSettings.value('serialport/baudrate')
        )
        self.ui.parityChooser.setCurrentText(
            globalSettings.value('serialport/parity')
        )
        self.ui.dataBitsChooser.setCurrentText(
            globalSettings.value('serialport/databits')
        )
        self.ui.stopBitsChooser.setCurrentText(
            globalSettings.value('serialport/stopbits')
        )
        self.ui.flowControlChooser.setCurrentText(
            globalSettings.value('serialport/flowcontrol')
        )

    def saveconfig(self):
        save_port(self.ui.serialPortChooser.currentText())
        save_baud(self.ui.baudrateChooser.currentText())
        save_parity(self.ui.parityChooser.currentText())
        save_databits(self.ui.dataBitsChooser.currentText())
        save_stopbits(self.ui.stopBitsChooser.currentText())
        save_flowcontrol(self.ui.flowControlChooser.currentText())

    def update_serial_port_list(self):
        self.ui.serialPortChooser.clear()
        for port in QSerialPortInfo.availablePorts():
            self.ui.serialPortChooser.addItem(port.portName())

    def update_program_list(self):
        self.ui.programListWidget.clear()
        self.dir.refresh()
        self.ui.programListWidget.addItems(
            self.dir.entryList()
        )
        self.ui.programListWidget.clearSelection()

    def selection_changed(self):
        if self.ui.serialPortChooser.currentText() is not None \
                and self.ui.programListWidget.currentItem() is not None:
            self.ui.sendButton.setEnabled(True)
        else:
            self.ui.sendButton.setDisabled(True)

    def refresh(self):
        self.update_program_list()
        self.update_serial_port_list()

    def send_program(self):
        selections = self.ui.programListWidget.selectedItems()
        for selection in selections:
            filename = selection.text()
            filepath = self.dir.path() + '/' + filename
            port_chosen = self.ui.serialPortChooser.currentText()
            confirm = ConfirmSend(self)
            confirm.ui.dialogLabel.setText(f'Send program \'{filename}\'?')
            confirm.exec()
            if confirm.result() == QDialog.Accepted:
                self.sender = Sender(
                    port_chosen,
                    filepath,
                    self.ui.baudrateChooser.currentText(),
                    self.ui.dataBitsChooser.currentText(),
                    self.ui.parityChooser.currentText(),
                    self.ui.stopBitsChooser.currentText(),
                    self.ui.flowControlChooser.currentText()
                )
                self.send_status = SendStatus(self, self.sender)
                self.send_status.show()
                self.sender.start()
                self.send_status.exec_()
                self.send_status.deleteLater()


class SerialProgramLoader(QMainWindow):
    def __init__(self):
        super(SerialProgramLoader, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loaderFrameLayout = QVBoxLayout(self.ui.loaderFrame)
        self.ui.loaderFrameLayout.setMargin(0)
        self.ui.loaderFrame.setLayout(self.ui.loaderFrameLayout)
        self.ui.loader = Loader(self)
        self.ui.loaderFrameLayout.addWidget(self.ui.loader)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Serial Program Loader')
    app.setApplicationVersion('0.0.0')
    parser = QCommandLineParser()
    parser.setApplicationDescription('Program to send Machining routines to '
                                     'CNC machines via serial port')
    startFullScreen = QCommandLineOption(('f', 'fullscreen'), "Start in fullscreen mode")
    parser.addOption(startFullScreen)
    parser.addHelpOption()
    parser.addVersionOption()
    parser.process(app)
    globalSettings = QSettings('settings.ini', QSettings.IniFormat)
    window = SerialProgramLoader()
    if parser.isSet(startFullScreen):
        window.showFullScreen()
    else:
        window.show()
    ret = app.exec_()
    sys.exit(ret)
