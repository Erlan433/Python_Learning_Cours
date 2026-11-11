import tkinter as tk


class AppListbox(tk.Listbox):
    def show_tasks(self, tasks):
        self.delete(0, tk.END)
        for task in tasks:
            self.insert(tk.END, task)
