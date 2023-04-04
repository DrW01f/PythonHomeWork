# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами
# элементы множеств.


def InputFunc():
    count1 = int(input("Введите кол-во элементов первого массива:  "))
    count2 = int(input("Введите кол-во элементов второго массива:  "))
    array1 = list()
    array2 = list()
    for i in range(count1):
        array1.append(int(input(f"Введите {i+1} элемент первого массива:  ")))
    for i in range(count2):
        array2.append(int(input(f"Введите {i+1} элемент второго массива:  ")))
    result = [0, 1]
    result[0] = array1
    result[1] = array2
    return result


def Calculating(array: list):
    lst1 = set(array[0])
    lst2 = set(array[1])
    result = list(lst1.intersection(lst2))
    result.sort()
    return result


def Main():
    arrays = InputFunc()
    result = Calculating(arrays)
    print(f"Общим среди {arrays[0]} и {arrays[1]} будет {result}")


Main()
