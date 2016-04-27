#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

class Window:

    def __init__(self):
        self.tk = Tk()
        # fullscreen manager
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # title
        Label(self.tk, text="D3EI", font=("Purisa", 40), anchor=CENTER).pack(side=TOP, padx=30, pady=30)
        # name_frame
        name_frame = Frame(self.tk, borderwidth=2, relief=GROOVE)
        name_frame.pack(side=TOP, padx=30, pady=30)
        self.name = StringVar()
        self.name.set("Random")
        Label(name_frame, text="Nom:", font=("Purisa", 20)).pack(side=LEFT, padx=30, pady=15)
        Entry(name_frame, textvariable=self.name, font=("Purisa", 18), width=100).pack(side=TOP, padx=30, pady=30)
        # conso_frame
        conso_frame = Frame(self.tk, borderwidth=2, relief=GROOVE)
        conso_frame.pack(side=TOP, padx=30, pady=30)
        self.conso = StringVar()
        self.conso.set("50L")
        Label(conso_frame, text="Consomation:", font=("Purisa", 20)).pack(side=LEFT, padx=30, pady=15)
        Label(conso_frame, textvariable=self.conso, font=("Purisa", 20)).pack(side=LEFT, padx=30, pady=15)
        # record_frame
        record_frame = Frame(self.tk, borderwidth=2, relief=GROOVE)
        record_frame.pack(side=TOP, padx=30, pady=30)
        self.mx = StringVar()
        self.mx.set("Random a le plus conssommé: 50L")
        self.mn = StringVar()
        self.mn.set("Random a le moins conssommé: 2L")
        Label(record_frame, textvariable=self.mx, font=("Purisa", 20)).pack(side=TOP, padx=30, pady=15)
        Label(record_frame, textvariable=self.mn, font=("Purisa", 20)).pack(side=TOP, padx=30, pady=15)
        # moyenne_frame
        moyenne_frame = Frame(self.tk, borderwidth=2, relief=GROOVE)
        moyenne_frame.pack(side=TOP, padx=30, pady=30)
        self.moyenne = StringVar()
        self.moyenne.set("20L")
        Label(moyenne_frame, text="Consomation moyenne:", font=("Purisa", 20)).pack(side=LEFT, padx=30, pady=15)
        Label(moyenne_frame, textvariable=self.moyenne, font=("Purisa", 20)).pack(side=LEFT, padx=30, pady=15)


    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
