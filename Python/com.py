import serial

# rep = serial.Serial("COM3",9600)
# while 1:
#     don=str(rep.readline())
#     print(don)


class Serial:
    def __init__(self):
        self.s = serial.Serial("COM3",9600)

    def get_msg(self):
        return str(self.s.readline())
