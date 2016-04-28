import threading
import time
from interface import Window
from com import Serial

stats = [{"name": "John", "conso": 20}, {"name": "Tom", "conso": 10}, {"name": "Bill", "conso": 15}]

window = Window()
arduino = Serial()

def minmax(array):
    M = 0
    m = 0
    for index in range(len(array)):
        item = array[index]
        if item["conso"] > array[M]["conso"]:
            M = index
        if item["conso"] < array[m]["conso"]:
            m = index
    return array[m], array[M]

def moyenne(array):
    myn = 0
    for item in array:
        myn += item["conso"]
    myn = myn/len(array)
    return myn

class Main(threading.Thread):
    def run(self):
        rdm = 0
        while 1:
            print(arduino)
            # Demarage
            if arduino.run.nb[0] == True:
                if "User" in window.name.get():
                    rdm += 1
                    window.name.set("User " + str(rdm))
                window.conso = "0L"
                stats.pop({"name": window.name.get(), "conso": 0})
            #
            myn = moyenne(stats)
            window.moyenne.set(str(myn)+"L")
            mn, mx = minmax(stats)
            window.mn.set(mn["name"] + " a le moins conssommé: " + str(mn["conso"]) + "L")
            window.mx.set(mx["name"] + " a le plus conssommé: " + str(mx["conso"]) + "L")
            time.sleep(2)

loop = Main()
loop.daemon = True
loop.start()
arduino.daemon = True
arduino.start()

window.tk.mainloop()
loop._stop()
