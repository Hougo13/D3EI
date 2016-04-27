import threading
import time
from interface import Window
from com import Serial

window = Window()
# arduino = Serial()
#
# print(arduino.get_msg())

class Main(threading.Thread):
    def run(self):
        while 1:
            print(window.name.get())
            window.name.set("coucou")
            print("ok")
            time.sleep(2)

loop = Main()
loop.daemon = True
loop.start()

window.tk.mainloop()
