import threading
import time
from interface import Window
from com import Serial

window = Window()
arduino = Serial()
arduino.nb = [0,False,False,False]

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

def findi(array, field, test):
    out = None
    for i in range(len(array)):
        if array[i][field] == test:
            out = i
    return out

class Main(threading.Thread):
    def run(self):
        stats = [{"name": "John", "conso": 20}, {"name": "Tom", "conso": 5}, {"name": "Bill", "conso": 15}]
        user = "User 1"
        window.name.set(user)
        stats.append({"name": window.name.get(), "conso": 0})
        rdm = 0
        while 1:
            
            # Demarage
            if arduino.nb[1] == True:
                arduino.nb[2] = False
                if "User" in window.name.get():
                    rdm += 1
                    user = "User " + str(rdm)
                    window.name.set(user)
                user = window.name.get()
                if not findi(stats, "name", user):
                    stats.append({"name": window.name.get(), "conso": 0})
                arduino.nb[1] = False

            print(stats)
            print(user)
            # Update quantity
            if not arduino.nb[2]:
                window.conso.set(str(arduino.nb[0])+"L")
                stats[findi(stats, "name", user)]["conso"] = arduino.nb[0]
                   
            myn = round(moyenne(stats))
            window.moyenne.set(str(myn)+"L")
            mn, mx = minmax(stats)
            window.mn.set(mn["name"] + " a le moins conssommé: " + str(mn["conso"]) + "L")
            window.mx.set(mx["name"] + " a le plus conssommé: " + str(mx["conso"]) + "L")
            #time.sleep(0.5)

loop = Main()
loop.start()
arduino.start()

window.tk.mainloop()
loop._stop()
