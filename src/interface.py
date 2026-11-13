import tkinter as tk
import math
from pathlib import Path

root = tk.Tk()
root.geometry("500x500")
root.title("Калькулятор")
root.iconbitmap(Path(__file__).resolve().parent.parent / "assets" / "image.ico")

buttons = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "/", "-", "+", "=", "C"]
operations = ["*", "/", "-", "+"]
expression = "0"

text_input = tk.Label(root, text="0", anchor="e", font=("Arial", 20), width=25)
text_input.place(x=45, y=30)


def click_button(value):
    global expression

    if value == "C":
        expression = "0"
    elif value == "=":
        try:
            expression = str(eval(expression))
        except (SyntaxError, ZeroDivisionError):
            expression = "Ошибка"
    elif expression == "0" and value not in operations:
        expression = value
    elif expression == "Ошибка" and value not in operations:
        expression = value
    else:
        expression += value

    text_input.config(text=expression)


index = 0
while index < len(buttons):
    angle = math.radians(index * 360 / len(buttons) - 90)
    x = 220 + 170 * math.cos(angle)
    y = 280 + 170 * math.sin(angle)
    tk.Button(
        root,
        text=buttons[index],
        width=6,
        height=2,
        command=lambda value=buttons[index]: click_button(value),
    ).place(x=x, y=y)
    index += 1

root.mainloop()