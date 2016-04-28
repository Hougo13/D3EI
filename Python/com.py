import serial
import re
import threading
import time

class Serial(threading.Thread):
    def run(self):
        self.co = False
        self.connect()
        while 1:
            if self.co == True:
                code=str(self.ser.readline())
                rest=list(code)
                num=0
                j = 0
                for i in range(len(rest)):
                    i = i - j
                    if (rest[i] == "b") or (rest[i] == "'")or (rest[i] == "r") or (rest[i] == "n") or (rest[i] == "\\"):
                        rest.pop(i)
                        j += 1
                if rest:
                    if rest[0] == "-":
                        num = -int(rest[1])
                    else:
                        if len(rest) > 1:
                            num = ""
                            for c in rest:
                                num = num+c
                            num = int(num)
                        else:
                            num = int(rest[0])

                if num >= 0:
                    self.nb[0] = num
                if num == -2:
                    self.nb[1] = True
                if num == -5:
                    self.nb[2] = True
                    
#                    resept = None
#                    try:
#                        resept = int(rest[i])
#                    except:
#                        continue
#                    if (rest[i]=="-")or((resept>-1)and(resept<10)):
#                        self.nb[num] = rest[i]
#                        num = num+1
                    #print(self.nb)
    def connect(self):
        try:
            self.ser = serial.Serial("COM3", 100, timeout=1)
            self.co = True
        except:
            print("Connection error")
            time.sleep(2)
            self.connect()
