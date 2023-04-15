# Задача 36: Напишите функцию
# print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по
# номеру строки и столбца. Аргументы num_rows и num_columns указывают
# число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def input_param_func() -> list:
    print("Для создания таблицы введите следующие данные")
    while True:
        num_rows = int(input("Введите количество строк"))
        if 0 < num_rows == 0:
            print("Ничего не получится, введите число больше 0")
        else:
            break
    while True:
        num_columns = int(input("Введите количество столбцов"))
        if 0 < num_columns == 0:
            print("Ничего не получится, введите число больше 0")
        else:
            break
    result=[num_rows, num_columns]
    return result
    


def main():
    input_parametrs = input_param_func()
    
    pass


main()
