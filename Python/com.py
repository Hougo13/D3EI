import serial
import re
import threading
import time

class Serial(threading.Thread):
    def run(self):
        co = False
        self.connect()
        self.nb = [0,0,0,0]
        while 1:
            if self.co == True:
                code=str(self.ser.readline())
                rest=list(code)
                nbrs=len(rest)
                num=0
                for i in range (0,nbrs):
                    if (rest[i]=="-")or(rest[i]=="1")or(rest[i]=="2")or(rest[i]=="3") :
                        self.nb[num] = rest[i]
                        num = num+1
    def connect(self):
        try:
            self.ser = serial.Serial("COM3", 9600, timeout=1)
            self.co = True
        except:
            print("Connection error")
            time.sleep(2)
            self.connect()
