# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'on_off.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial as ser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(256, 105)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 80))
        self.groupBox.setObjectName("groupBox")
        self.btn_on = QtWidgets.QPushButton(self.groupBox)
        self.btn_on.setGeometry(QtCore.QRect(10, 50, 89, 25))
        self.btn_on.setObjectName("btn_on")
        self.btn_off = QtWidgets.QPushButton(self.groupBox)
        self.btn_off.setGeometry(QtCore.QRect(110, 50, 89, 25))
        self.btn_off.setObjectName("btn_off")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.btn_off.clicked.connect(self.srOneOff)
        self.btn_on.clicked.connect(self.srOneOn)

    def srOneOn(self):
            print("srone is on")
            cmd = "x"
            byt = [ord(c) for c in cmd]
            ser.Serial()
            ser.Serial('COM3', 9600,bytesize = 8, stopbits=2)
            
            
    def srOneOff(self):
            print("srone is off")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "SR one ON and OFF"))
        self.btn_on.setText(_translate("MainWindow", "On"))
        self.btn_off.setText(_translate("MainWindow", "Off"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

