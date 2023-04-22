# Задача №49. Решение в группах Создать телефонный справочник с
# возможностью импорта и экспорта данных в формате .txt. Фамилия, имя,
# отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и
# удаления данных. Пользователь также может ввести имя или фамилию, и Вы
# должны реализовать функционал для изменения и удаления данных

import os
import json

"""
данные в файле будут храниться в виде списка словарей!
os.getcwd() - текущая рабочая директория.
os.listdir(path=".") - список файлов и директорий в папке.
"""


def full_name_file(name="phone_book", extension=".txt") -> str:
    """
    Функция для возвращения имени файла (при работе в текущей директории)
    """
    return name + extension


def create_file(file_name: str) -> None:
    """
    Функция для создания файла
    """
    if file_name not in os.listdir(os.getcwd()):
        file = open(file_name, "w", encoding="UTF-8")
        file.write("[]")
        print(f'Создан файл: {file_name}')


def load_info() -> list:
    """
    Загружает данные из файла
    """
    name = full_name_file()
    with open(name, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_info(data: list) -> None:
    """
    Функция добавляет новый контакт
    """
    data.append(
            dict(
                first_name=input("Введите имя контакта:\n"),
                second_name=input("Введите фамилию контакта:\n"),
                phone_number=input("Введите номер телефона:\n")            
                )
            )
    print("Контакт успешно добавлен")


def save_info(data: list) -> None:
    """
    Функция для сохранения информации в файл
    """
    name = full_name_file()
    with open(name, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False)


def show_info(phone_book: list) -> None:
    """
    Функция выводит на экран содержание справочника
    """
    if len(phone_book) < 1:
        print("Справочник пока пуст")
    else:
        phone_dict = dict(
                first_name= "Имя",
                second_name="Фамилия",
                phone_number="Номер телефона"            
                )
        info = str()
        for num, elem in enumerate(phone_book, 1):
            info += f"\nКонтакт №{num}:\n"
            info += "\n".join(f"{phone_dict[k]}:  {v}" for k, v in elem.items())
            info += "\n---------------\n"
        print(info)


def delete_info(data: list)-> None:
    """
    Функция удаляет контакт(элемент списка) из телефонного справочника
    """
    if len(data) > 0:
        while True:
            try:
                number = int(input("Выберите номер контакта, который хотите удалить: \n(0 - показать контакты) \n-1 прервать команду\n"))
                if number == 0:
                    show_info(data)
                elif number == -1:
                    break
                elif 1 <= number < len(data) +1:
                    data.pop(number - 1)
                    print(f"\nКонтакт № {number} успешно удален")            
                    break
                else:
                    print("Такого номера контакта не существует")
            except ValueError:
                print("Введено неправильное значение")
    else:
        print("Справочник пока пуст")


def find_contact(data: list)->None:
    """
    Функция для поиска контакта
    """
    if len(data) > 0:
        find = input("Введите значение для поиска:  ")
        result = list(filter(lambda elem: find in elem["first_name"] or find in elem["second_name"] or find in elem["phone_number"], data))
        if result:
            print(f"Найдено {len(result)} контакта(ов): \n")
            show_info(result)
        else:
            print("Ничего не найдено")
    else:
        print("Справочник пока пуст")


def change_info(data: list)->None:
    """
    Функция изменяет значение контактов по выбору параметра
    """
    if len(data) > 0:
        while True:
            try:
                number = int(input("\nВыберите номер контакта, который хотите изменить: \n(0 - показать контакты, -1 прервать команду)\n"))
                if number == 0:
                    show_info(data)
                elif number == -1:
                    break
                elif 1 <= number < len(data) +1:
                    while True:
                        elem = data[number-1]
                        change = input("Выберите параметр для изменения: Ф - фамилия, И - имя, Н - номер телефона (-1 - прервать команду):\n")
                        if change == "-1":
                                break                            
                        elif change.lower() == "и":
                            elem["first_name"] = input("Введите новое имя:\n")
                        elif change.lower() == "ф": 
                            elem["second_name"] = input("Введите новую фамилию:\n")
                        elif change.lower() == "н":
                            elem["phone_number"] = input("Введите новый номер телефона:\n")
                        else:
                            print("Введено неправильное значение")
                    
                    print(f"Контакт № {number} успешно изменен")            
                    break
                else:
                    print("Такого номера контакта не существует")
            except ValueError:
                print("Введено неправильное значение")
    else:
        print("Справочник пока пуст")



def menu()-> int:
    """
    Функция возвращает значение порядкого номера команды из всех возможных
    """
    command = {
        "exit" : "Закончить работу",
        "show": "Показать содержимое телефонного справочника", 
        "add": "Добавить новый контакт", 
        "find": "Найти контакт",
        "change" : "Изменить контакт",
        "delete" : "Удалить контакт"
        }         
    
    while True:        
        choice = input("Нажмите цифру команды или введите 'help' для получения справки(0 - завершение работы): ")
        if choice.isdigit():
            if 0 <= int(choice) < len(command):
                return(int(choice))
            else:
                print("Такой команды пока нет")
        elif choice.lower() == "help":
            print("На данный момент программа обладает следующими возможностями:")        
            for num, val in enumerate(command.values()):
                print(num, val)
        else:
            print("Неизвестная команда")
         
 
def main():
    """
    Главная функция
    """
    name = full_name_file()
    create_file(name)
    data = load_info()
   
    while True:
        command = menu()    
        if command == 0:            
            print("Личинка skynet закончила свою работу")
            return
        elif command == 1:
            show_info(data)
        elif command == 2:
            create_info(data)
        elif command == 3:
            find_contact(data) 
        elif command == 4:
            change_info(data) 
        elif command == 5:
            delete_info(data)
        save_info(data)   
        
if __name__ == '__main__':
    main()
