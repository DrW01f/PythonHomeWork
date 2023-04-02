# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

def InputArray():
    parametrs = [0, 0]  # массив, ближайшее
    count = int((input('Введите количество элементов в массиве:  ')))
    lst = []

    for i in range(count):
        lst.append(int(input(f'Введите элемент номер {i + 1}:  ')))
    parametrs[0] = lst
    parametrs[1] = int((input('Введите элемент X:  ')))
    return parametrs


def Difference(array):
    nearest = array[0][0]  # Считаем первое число ближайшим 
    diff = abs(array[0][0] - array[1])# считаем разницу между ними минимальной

    for i in array[0]:
        if abs(i - array[1]) < diff:
            diff = abs(i - array[1])
            nearest = i
    
    return nearest


def Main():
    array = InputArray()
    result = Difference(array)
    print(f"Ближайшим числом к искомому {array[1]} является {result}")
    


Main()
