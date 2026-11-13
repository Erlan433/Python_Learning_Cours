"""Reusable Tkinter widgets with one visual style."""

import tkinter as tk


BACKGROUND = "#f3f4f6"
SURFACE = "#ffffff"
PRIMARY = "#4f46e5"
TEXT = "#111827"


class AppLabel(tk.Label):
    def __init__(self, master, text: str = "", **kwargs) -> None:
        defaults = {"bg": BACKGROUND, "fg": TEXT, "font": ("Segoe UI", 11)}
        defaults.update(kwargs)
        super().__init__(master, text=text, **defaults)


class AppEntry(tk.Entry):
    def __init__(self, master, **kwargs) -> None:
        defaults = {
            "font": ("Segoe UI", 11),
            "bg": SURFACE,
            "fg": TEXT,
            "relief": tk.SOLID,
            "bd": 1,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class AppButton(tk.Button):
    def __init__(self, master, text: str, command, **kwargs) -> None:
        defaults = {
            "font": ("Segoe UI", 10, "bold"),
            "bg": PRIMARY,
            "fg": "white",
            "activebackground": "#4338ca",
            "activeforeground": "white",
            "relief": tk.FLAT,
            "cursor": "hand2",
            "padx": 10,
            "pady": 6,
        }
        defaults.update(kwargs)
        super().__init__(master, text=text, command=command, **defaults)


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs) -> None:
        defaults = {
            "font": ("Segoe UI", 11),
            "bg": SURFACE,
            "fg": TEXT,
            "selectbackground": PRIMARY,
            "selectforeground": "white",
            "activestyle": "none",
            "relief": tk.SOLID,
            "bd": 1,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class AppFrame(tk.Frame):
    def __init__(self, master, **kwargs) -> None:
        defaults = {"bg": BACKGROUND}
        defaults.update(kwargs)
        super().__init__(master, **defaults)
