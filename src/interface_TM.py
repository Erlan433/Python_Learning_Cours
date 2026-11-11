import tkinter as tk
from pathlib import Path


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Task Manager")
        self.root.iconbitmap(Path(__file__).resolve().parent.parent / "assets" / "image.ico")
