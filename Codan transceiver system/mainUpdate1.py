from PyQt5 import QtGui, QtWidgets
from mainGUIUpdate1 import Ui_MainWindow
import serial
import time
import threading

class MyGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial()
        self.setupUi(self)
        self.setupSerialParameter()
        self.CmdPtt()
        self.cmdScan()

        self.btnScan.clicked.connect(self.scanOnOff)
        self.btnPtt.clicked.connect(self.pttOnOffbtn)
        self.btnSingleChan.clicked.connect(self.setChannel)
        self.btnMultChan.clicked.connect(self.multiChannelTH)
        self.btnMultChanStop.clicked.connect(self.stopIteration)
        self.cmbMode.currentIndexChanged.connect(self.cmdMode)
    
    def setupSerialParameter(self):
        self.ser.port = 'COM7'
        self.ser.baudrate = 9600
        self.ser.timeout = 0.5
        self.ser.open()
    
    def CmdPtt(self):
        
        fullCommandPtt = 'ptt'+'\r'
        askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
        self.ser.write(askyP) # send/ Write the ascii code to the serial port
        valPtt = self.ser.read(100)
        pttVal = (str(valPtt).strip()[14:17]) # strip method cuts out unnesessary characters received from serial port
        
        if "\\" in pttVal:
            self.btnPtt.setText(pttVal.strip()[:2])
        else:
            self.btnPtt.setText(pttVal)
    
    def cmdScan(self):
        
        fullCommandPtt = 'scan'+'\r'
        askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
        self.ser.write(askyP) # send/ Write the ascii code to the serial port
        valPtt = self.ser.read(100) # read 100 bytes of data from the serial port
        pttVal = (str(valPtt).strip()[16:19]) # strip method cuts out unnesessary characters received from serial port
        if "," in pttVal:
            self.btnScan.setText(pttVal.strip()[:2])# strip method cuts out unnesessary characters received from serial port
        else:
            self.btnScan.setText(pttVal)
    
    def scanOnOff(self):
        string = self.btnScan.text()
        if "\\" in string or string == "ON":
            fullCommandPtt = 'scan off'+'\r'
            askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
            self.ser.write(askyP) # send/ Write the ascii code to the serial port
            self.btnScan.setText('OFF')
        else:
            fullCommandPtt = 'scan on'+'\r'
            askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
            self.ser.write(askyP) # send/ Write the ascii code to the serial port
            self.btnScan.setText('ON')

    def pttOnOffbtn(self):        
        string = self.btnPtt.text()
        self.pttSwitch(string)

    def pttSwitch(self, string):
        if "\\" in string or string == "ON":
            fullCommandPtt = 'ptt off'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnPtt.setText("OFF")
        else:
            fullCommandPtt = 'ptt on'+'\r'
            askyP = [ord(c) for c in fullCommandPtt]
            self.ser.write(askyP)
            self.btnPtt.setText("ON")

    def setChannel(self):
        # check scanning mode
        self.ser.flushInput()# to clear serial input buffer
        fullCommandPtt = 'scan'+'\r'
        askyP1 = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
        self.ser.write(askyP1) # send/ Write the ascii code to the serial port
        valPtt = self.ser.read(100)
        pttVal = (str(valPtt).strip()[16:19])
        if "," in pttVal:
            print(pttVal)
            fullCommandPtt = 'scan off'+'\r'
            askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
            self.ser.write(askyP) # send/ Write the ascii code to the serial port
            self.btnScan.setText('OFF')

        chanName = self.txtChan.text()
        fullCommandPtt = "chan "+"\""+"ch 0"+""+chanName+"\"\r"
        askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
        self.ser.write(askyP) # send/ Write the ascii code to the serial port

    def multiChannelTH(self):
        self.ser.flushInput()# to clear serial input buffer
        fullCommandPtt = 'scan'+'\r'
        askyP1 = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
        self.ser.write(askyP1) # send/ Write the ascii code to the serial port
        valPtt = self.ser.read(100)
        pttVal = (str(valPtt).strip()[16:19])
        if "," in pttVal:
            print(pttVal)
            fullCommandPtt = 'scan off'+'\r'
            askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
            self.ser.write(askyP) # send/ Write the ascii code to the serial port
            self.btnScan.setText('OFF')
            self.btnScan.setEnabled(False) #Didabled while looping throught the channels

        tr = threading.Thread(target=self.multiChannel,)
        tr.start()
    
    def multiChannel(self):
        self.loopCtrl = True
        while self.loopCtrl:
            i = 1
            while i<6:
                fullCommandPtt = "chan "+"\""+"ch 0"+""+str(i)+"\"\r"
                if self.loopCtrl == False:
                    break                    
                askyP = [ord(c) for c in fullCommandPtt]
                self.ser.write(askyP)
                self.pttOnOff("ON")
                time.sleep(1)
                self.pttOnOff("OFF")
                i+=1

    def stopIteration(self):
        self.loopCtrl = False # Stoping the iteration thread
        self.btnScan.setEnabled(False) # back to function after stoping channel  iteration

    def pttOnOff(self, Ptt):
        if Ptt == "ON":
            fullCommandPtt = 'ptt on'+'\r'
            askyP = [ord(c) for c in fullCommandPtt] # ord method convert each character to ascii values
            self.ser.write(askyP) # send/ Write the ascii code to the serial port
            self.btnPtt.setText("ON")
        else:
            fullCommandPtt = 'ptt OFF'+'\r'
            askyP = [ord(c) for c in fullCommandPtt] # ord convert each character to ascii values
            self.ser.write(askyP) # send/ Write the ascii code to the serial port
            self.btnPtt.setText("OFF")

    def cmdMode(self):
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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    sys.exit(app.exec_())