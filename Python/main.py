from interface import Window
from com import Serial

window = Window()
arduino = Serial()

print(arduino.get_msg())

window.tk.mainloop()
