import serial
rep = serial.Serial("COM3",9600)
while 1:
    don=str(rep.readline())
    print(don)

