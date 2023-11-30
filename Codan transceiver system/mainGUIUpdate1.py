# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUIUpdate1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 681, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 37, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(470, 67, 47, 21))
        self.label_3.setObjectName("label_3")
        self.btnScan = QtWidgets.QPushButton(self.groupBox)
        self.btnScan.setGeometry(QtCore.QRect(570, 37, 75, 23))
        self.btnScan.setObjectName("btnScan")
        self.btnPtt = QtWidgets.QPushButton(self.groupBox)
        self.btnPtt.setGeometry(QtCore.QRect(570, 67, 75, 23))
        self.btnPtt.setObjectName("btnPtt")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 10, 20, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(470, 100, 101, 20))
        self.label_4.setObjectName("label_4")
        self.cmbMode = QtWidgets.QComboBox(self.groupBox)
        self.cmbMode.setGeometry(QtCore.QRect(570, 97, 71, 22))
        self.cmbMode.setObjectName("cmbMode")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.label_5.setObjectName("label_5")
        self.txtChan = QtWidgets.QLineEdit(self.groupBox)
        self.txtChan.setGeometry(QtCore.QRect(100, 50, 101, 20))
        self.txtChan.setObjectName("txtChan")
        self.btnSingleChan = QtWidgets.QPushButton(self.groupBox)
        self.btnSingleChan.setGeometry(QtCore.QRect(60, 110, 81, 23))
        self.btnSingleChan.setObjectName("btnSingleChan")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(200, 10, 20, 131))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(220, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btnMultChan = QtWidgets.QPushButton(self.groupBox)
        self.btnMultChan.setGeometry(QtCore.QRect(220, 110, 101, 23))
        self.btnMultChan.setObjectName("btnMultChan")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(220, 40, 91, 21))
        self.label_8.setObjectName("label_8")
        self.txtChanStart = QtWidgets.QLineEdit(self.groupBox)
        self.txtChanStart.setGeometry(QtCore.QRect(320, 40, 113, 20))
        self.txtChanStart.setObjectName("txtChanStart")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(220, 70, 91, 21))
        self.label_9.setObjectName("label_9")
        self.txtChanStop = QtWidgets.QLineEdit(self.groupBox)
        self.txtChanStop.setGeometry(QtCore.QRect(320, 70, 113, 20))
        self.txtChanStop.setCursorPosition(1)
        self.txtChanStop.setObjectName("txtChanStop")
        self.btnMultChanStop = QtWidgets.QPushButton(self.groupBox)
        self.btnMultChanStop.setGeometry(QtCore.QRect(350, 110, 91, 23))
        self.btnMultChanStop.setObjectName("btnMultChanStop")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(450, 10, 20, 121))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(470, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transceiver controlling System"))
        self.label_2.setText(_translate("MainWindow", "Scanning"))
        self.label_3.setText(_translate("MainWindow", "PTT"))
        self.btnScan.setText(_translate("MainWindow", "ON"))
        self.btnPtt.setText(_translate("MainWindow", "ON"))
        self.label_4.setText(_translate("MainWindow", "Modulation Mode"))
        self.cmbMode.setItemText(0, _translate("MainWindow", "USB"))
        self.cmbMode.setItemText(1, _translate("MainWindow", "LSB"))
        self.cmbMode.setItemText(2, _translate("MainWindow", "AM"))
        self.cmbMode.setItemText(3, _translate("MainWindow", "USBW"))
        self.cmbMode.setItemText(4, _translate("MainWindow", "LSBW"))
        self.cmbMode.setItemText(5, _translate("MainWindow", "USBWX"))
        self.cmbMode.setItemText(6, _translate("MainWindow", "LSBWX"))
        self.cmbMode.setItemText(7, _translate("MainWindow", "UMCW"))
        self.cmbMode.setItemText(8, _translate("MainWindow", "LMCW"))
        self.label_5.setText(_translate("MainWindow", "Channel"))
        self.btnSingleChan.setText(_translate("MainWindow", "Set Channel"))
        self.label_6.setText(_translate("MainWindow", "Single channel Mode"))
        self.label_7.setText(_translate("MainWindow", "Multi channel Mode"))
        self.btnMultChan.setText(_translate("MainWindow", "Start Iteration"))
        self.label_8.setText(_translate("MainWindow", "Start Channel"))
        self.txtChanStart.setText(_translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "Stop Channel"))
        self.txtChanStop.setText(_translate("MainWindow", "5"))
        self.btnMultChanStop.setText(_translate("MainWindow", "Stop Iteration"))
        self.label_10.setText(_translate("MainWindow", "Status "))
