# ROADMAP.md — Task Manager

---

## Версия → Задача

---

### ![v0.0.1](https://img.shields.io/badge/version-0.0.1-blue) — Каркас приложения

- [x] разработан цикл приложения — структурное программирование
- [x] список задач в памяти (`collection = []`)

---

### ![v0.0.2](https://img.shields.io/badge/version-0.0.2-blue) — Ввод задач

- [x] внедрён i/o функционал для ввода задачи
- [x] проверка: пустой ввод не добавляется
- [x] проверка: дубликат по имени не добавляется

---

### ![v0.0.3](https://img.shields.io/badge/version-0.0.3-blue) — Функции цикла

- [x] разработаны функции для цикла — функциональное программирование
- [x] `show_collection` — вывод списка с нумерацией
- [x] `show_message` — сообщение + пауза

---

### ![v0.0.4](https://img.shields.io/badge/version-0.0.4-blue) — Проверки и подтверждения

- [x] добавлены проверки и подтверждения
- [x] `check_confirm` — спросить Y/N перед выходом

---

### ![v0.0.5](https://img.shields.io/badge/version-0.0.5-blue) — Файловые сохранения

- [x] созданы методы сохранения и загрузки — файловые сохранения
- [x] `storage.load_collection` / `storage.save_collection`
- [x] `utils.ensure_save_file` — создаёт `saves.txt` при первом запуске
- [x] `utils.get_base_dir` — работает и для `.py`, и для `.exe`

---

### ![v0.0.6](https://img.shields.io/badge/version-0.0.6-blue) — Логика вне цикла

- [x] созданы методы для удаления, редактирования и создания задач — логика вынесена из цикла
- [x] `core.create_task`, `core.edited_task`, `core.deleated_task`

---

### ![v0.0.7](https://img.shields.io/badge/version-0.0.7-blue) — Точка входа

- [x] основной цикл помещён в отдельный метод — `def main`
- [x] `main.py` + `app.py` разделены
- [x] `if __name__ == "__main__"` защита

---

### ![v0.0.8](https://img.shields.io/badge/version-0.0.8-blue) — Контент задачи

- [x] реализован функционал добавления контента задачи — имя + содержание
- [x] формат хранения: `"имя описание"` одной строкой

---

### ![v0.0.9](https://img.shields.io/badge/version-0.0.9-blue) — Модульная разгрузка

- [x] разгруппировка по модулям, тестирование всего функционала
- [x] `config`, `utils`, `storage`, `view`, `core`, `app`, `main` — разделены
- [x] docstring в каждом модуле

---

### ![v0.1.0](https://img.shields.io/badge/version-0.1.0-blue) — Сборка и документация

- [x] добавлены методы самоопределения приложения
- [x] разработана документация
- [x] выполнена сборка (PyInstaller)
- [x] `get_base_dir` работает и в `.exe`, и в `.py`

---

### ![v0.1.1](https://img.shields.io/badge/version-0.1.1-green) — Структура src и первый GUI

- [x] архитектурная коррекция — модули в `src/` по директориям
- [x] создание первичного GUI
- [x] `src/` с `__init__.py`
- [x] `src/ui/` с `__init__.py`
- [x] перенос консольных модулей в `src/`

---

### ![v0.1.2](https://img.shields.io/badge/version-0.1.2-green) — Основные экраны Tkinter

- [x] создание основных методов view-модуля с взаимодействиями через tkinter
- [x] `init()` — создаёт `frame_menu` / `frame_tasks`
- [x] `create_menu()` / `show_all_tasks()` — переключение экранов
- [x] `show_tasks` через `Listbox`

---

### ![v0.1.3](https://img.shields.io/badge/version-0.1.3-orange) — Кастомные компоненты

- [x] создание кастомных компонентов — `AppButton`
- [x] `ui/Button.py` с `class AppButton(tk.Button)`
- [x] `super().__init__` с `master`, `text`, `command`, `**kwargs`
- [x] дефолты: `width=16`, `height=1`, `bg="#333333"`
- [x] переопределение через `bg="red"` у кнопки «Выход» работает

---

### v0.1.4 — Обновление Task Manager

- [x] созданы `AppLabel`, `AppButton` и `AppListbox`
- [x] добавлены ввод и отображение задач в GUI
- [x] сохранение задач переведено из TXT в JSON

---
