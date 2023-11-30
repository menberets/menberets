import sys
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui, QtWidgets
from mainGUI import Ui_MainWindow
import serial
import time
import threading
class MyGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.setupSerialParameter()
        # self.StatusHandler()
        self.CmdPtt()
        self.cmdScan()
        # self.cmdMode()

        fullCommandPtt = 'mode'+'\r'
        askyP = [ord(c) for c in fullCommandPtt]
        self.ser.write(askyP)
        valPtt = self.ser.read(100)
        cmdText = str(valPtt).strip()[16:20]
        print(cmdText)

      


        self.loopCtrl = True
        self.btnSingleChan.clicked.connect(self.setChannel)
        self.btnMultChan.clicked.connect(self.multiChannelTH)
        self.btnPtt.clicked.connect(self.pttOnOffbtn)
        self.btnScan.clicked.connect(self.scanOnOff)
        self.btnMultChanStop.clicked.connect(self.stopIteration)
        self.cmbMode.currentIndexChanged.connect(self.cmdMode)
        # self.cm
    def setupSerialParameter(self):
        self.ser.port = 'COM7'
        self.ser.baudrate = 9600
        self.ser.timeout = 0.5
        self.ser.open()
    
    def scanOnOff(self):
        string = self.btnScan.text()
        if "\\" in string or string == "ON":
            fullCommandPtt = 'scan off'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnScan.setText('OFF')
        else:
            fullCommandPtt = 'scan on'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnScan.setText('ON')
        # print("Scan on off")
    def pttOnOffbtn(self): #535 1603
        # print(self.btnPtt.text == Ptt)
        string = self.btnPtt.text()
        # str(valPtt).strip()[14:19]
        if "\\" in string or string == "ON":# and self.btnPtt.text == 'ON' :
            # print("TRUE")
            fullCommandPtt = 'ptt off'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnPtt.setText("OFF")
        else:
            print("FALSE")
            fullCommandPtt = 'ptt on'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnPtt.setText("ON")
    def pttOnOff(self, Ptt): #535 1603
        # print(self.btnPtt.text == Ptt)
        # string = self.btnPtt.text()
        # str(valPtt).strip()[14:19]
        if Ptt == "ON":# and self.btnPtt.text == 'ON' :
            # print("TRUE")
            fullCommandPtt = 'ptt on'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnPtt.setText("ON")
        else:
            print("FALSE")
            fullCommandPtt = 'ptt OFF'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnPtt.setText("OFF")

    def setChannel(self):
        chanName = self.txtChan.text()
        
        fullCommandPtt = "chan "+"\""+"ch 0"+""+chanName+"\"\r"
        # print(fullCommandPtt)
        askyP = [ord(c) for c in fullCommandPtt]
        self.ser.write(askyP)
    def cmdMode(self):
        # fullCommandPtt = 'mode'+'\r'
        # askyP = [ord(c) for c in fullCommandPtt]
        # self.ser.write(askyP)
        # valPtt = self.ser.read(100)
        # cmdText = str(valPtt).strip()[16:20]
        # # print(cmdText)
        # self.cmbMode.setCurrentText(cmdText) 
        # # print(cmdText)
        mode = self.cmbMode.currentText()
        if mode == "LSB":
            fullCommandPtt = 'mode LSB'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "USB":
            fullCommandPtt = 'mode USB'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "AM":
            fullCommandPtt = 'mode AM'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "CW":
            fullCommandPtt = 'mode CW'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "LSBW":
            fullCommandPtt = 'mode LSBW'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "USBW":
            fullCommandPtt = 'mode USBW'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "UMCW":
            fullCommandPtt = 'mode UMCW'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        elif mode == "LMCW":
            fullCommandPtt = 'mode LMCW'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
        
    # def cmdScan(self):
    #     fullCommandPtt = 'scan'+'\r'
    #     askyP = [ord(c) for c in fullCommandPtt]
    #     self.ser.write(askyP)
    #     valPtt = self.ser.read(100)
    #     self.btnScan.setText(str(valPtt).strip()[15:19])
        
    def CmdPtt(self):
        
        fullCommandPtt = 'ptt'+'\r'
        askyP = [ord(c) for c in fullCommandPtt]
        self.ser.write(askyP)
        valPtt = self.ser.read(100)
        pttVal = (str(valPtt).strip()[14:17])
        
        if "\\" in pttVal:
            self.btnPtt.setText(pttVal.strip()[:2])
        else:
            self.btnPtt.setText(pttVal)
    def cmdScan(self):
        
        fullCommandPtt = 'scan'+'\r'
        askyP = [ord(c) for c in fullCommandPtt]
        self.ser.write(askyP)
        valPtt = self.ser.read(100)
        pttVal = (str(valPtt).strip()[16:19])
        print(pttVal)
        if "," in pttVal:
            self.btnScan.setText(pttVal.strip()[:2])
        else:
            self.btnScan.setText(pttVal)
    def multiChannelTH(self):
        tr = threading.Thread(target=self.multiChannel,)
        tr.start()
    
    def multiChannel(self):
        
        self.loopCtrl = True
        while self.loopCtrl:
            i = 1
            while i<6:
               
                fullCommandPtt = "chan "+"\""+"ch 0"+""+str(i)+"\"\r"
                # print(fullCommandPtt)
                if self.loopCtrl == False:
                    break                    
                askyP = [ord(c) for c in fullCommandPtt]
                self.ser.write(askyP)
                self.pttOnOff("ON")
                time.sleep(1)
                
                self.pttOnOff("OFF")
                i+=1
    
    def stopIteration(self):
        self.loopCtrl = False
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    sys.exit(app.exec_())