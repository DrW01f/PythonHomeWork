# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых
# чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

def Array():
    parametrs = [0, 0]  # для возврата из функции (сам массив, искомое)
    count = int((input('Введите количество элементов в массиве:  ')))
    lst = []

    for i in range(count):
        lst.append(int(input(f'Введите элемент номер {i + 1}:  ')))
    parametrs[0] = lst
    parametrs[1] = int((input('Введите искомый элемент:  ')))
    return parametrs


def Calculating(array):
    count = 0
    for i in array[0]:
        if i == array[1]:
            count += 1
    return count


def Main():
    inputList = Array()
    count = Calculating(inputList)
    print(f"Число {inputList[1]} встречается {count} раз(а)")


Main()
