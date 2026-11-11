import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, font=("Arial", 12), **kwargs)
