""" =========================================================
        Модуль для дополнительных функций приложения
    =========================================================
"""

import os
import sys

"""подтверждение действия"""


def check_confirm(action: str):
    confirm = input("точно?\nY/N: ").strip().upper()
    if confirm.startswith(("Y", "Д")):
        print(action)
        return False

    print("отмена")
    return True


"""Папка, где лежит EXE (или .py при разработке)."""


def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


"""Если файла нет — создаёт с дефолтным содержимым."""


def ensure_save_file(file_name=None):
    if file_name is None:
        file_name = os.path.join(get_base_dir(), "saves.txt")

    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8"):
            pass

    return file_name


# В формулировке задания функция названа insure_save_file.
insure_save_file = ensure_save_file
