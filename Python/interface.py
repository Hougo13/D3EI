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
        title = Label(self.tk, text="D3EI", font=("Purisa", 40))
        title.pack(side=TOP, pady=15)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
