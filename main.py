"""
    Точка входа в приложение Task Manager
    version 0.0.3
    --- description ---
    - [x] создать редактирование задач
    - [x] реализовать удаление задачи
"""

def show_message (choise):
    match choise:
        case "2":
            print('Задача успешно добавлена!')
        case "3":
            print('Задача успешно изменена!')
        case "4":
            print('Задача успешно удалена!')
    
    
def show_collection (collections):
    for key, item in enumerate(collections):
        print(f"{key+1}) {item}")
        
def error_msg ():
    print("Ошибка! Такого номера задачи нет!")


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
            show_collection(collections)
            
        case "2":
            collections.append(input("Введите название задачи: "))
            show_message(choise)
            
        case "3":
            show_collection(collections)
            try:
                select_edit = int(input("Введите номер задачи: "))
                edit_name = input("Введите новое имя задачи: ")
                collections[select_edit - 1] = edit_name
                show_message(choise)
            except:
                error_msg()
                
        case "4":
            show_collection(collections)
            try:
                delete_edit = int(input("Введите номер задачи: "))
                collections.pop(delete_edit - 1)
                show_message(choise)
            except:
                error_msg()

        case "5":
            is_run = False
            print("Прощай")
            
        case _:
            print("Такого пункта нету")
