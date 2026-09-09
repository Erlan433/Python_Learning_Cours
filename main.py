"""
    Точка входа в приложение Task Manager
    version 0.0.3
    --- description ---
    - [x] создать редактирование задач
    - [x] реализовать удаление задачи
"""

is_run = True
collections = []

print("Добро пожаловать!")
while is_run:
    print("\n------ Меню ------\n"
          "1. Посмотреть все задачи\n"
          "2. Добавить задачу\n"
          "3. Редактировать задачу\n"
          "4. Удаленить задачу\n"
          "5. Выйти\n")
    choise = input("Ваш выбор: ")
    match choise:
        case "1":
            for key, item in enumerate(collections):
                print(key+1, item)
        case "2":
            collections.append(input("Введите название задачи: "))
        case "3":
            for key, item in enumerate(collections):
                print(key + 1, item)
            try:
                select_edit = int(input("Введите номер задачи: "))
                edit_name = input("Введите новое имя задачи: ")
                collections[select_edit - 1] = edit_name
            except:
                print("Ошибка! Такого номера задачи нет!")
        case "4":
            for key, item in enumerate(collections):
                print(key + 1, item)
            try:
                delete_edit = int(input("Введите номер задачи: "))
                collections.pop(delete_edit - 1)
            except:
                print("Ошибка! Такого номера задачи нет!")

        case "5":
            is_run = False
            print("Прощай")
        case _:
            print("Такого пункта нету")
