import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, text=text, command=command, width=16, **kwargs)
