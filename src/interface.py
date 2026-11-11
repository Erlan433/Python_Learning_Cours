import tkinter as tk
from pathlib import Path

root = tk.Tk()
root.geometry("400x400")
root.title("Tkinter")
root.iconbitmap(Path(__file__).resolve().parent.parent / "assets" / "image.ico")

button = tk.Button(root, text="Кнопка")
button.pack()

label = tk.Label(root, text="Текст")
label.pack()

root.mainloop()
