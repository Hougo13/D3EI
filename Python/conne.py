import serial
import re
nb = [0,0,0,0]
ser = serial.Serial("COM3",100,timeout=1)
while 1:
    code=str(ser.readline())
    rest=list(code)
    nbrs=len(rest)
    num=0
    for i in range (0,nbrs):
        if (rest[i]=="-")or(rest[i]=="1")or(rest[i]=="2")or(rest[i]=="3")or(rest[i]=="4")or(rest[i]=="5")or(rest[i]=="6")or(rest[i]=="7")or(rest[i]=="8")or(rest[i]=="9") :
            nb[num] = rest[i]
            num = num+1
        print(nb)
    
