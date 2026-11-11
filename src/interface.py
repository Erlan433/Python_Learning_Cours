import tkinter as tk
from pathlib import Path

root = tk.Tk()
root.geometry("300x360")
root.title("Калькулятор")
root.iconbitmap(Path(__file__).resolve().parent.parent / "assets" / "image.ico")

operations = ["*", "/", "-", "+", "="]
expression = ""

text_input = tk.Label(root, text="", anchor="e", font=("Arial", 20), width=18)
text_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def click_button(value):
    global expression

    if value == "=":
        try:
            expression = str(eval(expression))
        except (SyntaxError, ZeroDivisionError):
            expression = "Ошибка"
    else:
        expression += value

    text_input.config(text=expression)


for number in range(10):
    row = number // 3 + 1
    column = number % 3
    tk.Button(
        root,
        text=str(number),
        width=6,
        height=2,
        command=lambda value=str(number): click_button(value),
    ).grid(row=row, column=column, padx=2, pady=2)

for index in range(len(operations)):
    tk.Button(
        root,
        text=operations[index],
        width=6,
        height=2,
        command=lambda value=operations[index]: click_button(value),
    ).grid(row=index + 1, column=3, padx=2, pady=2)

root.mainloop()
