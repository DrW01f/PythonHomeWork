# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, 
# -5, 7]
# Диапазон от 6 до 12
# Вывод: [1, 9, 13, 14, 19]

import random

def main():
    upper_limit = int(input("Введите верхнюю границу:  "))
    lower_limit = int(input("Введите нижнюю границу:  "))
    array = [random.randint(-50, 50) for i in range(20)]
    print(f"Текущий список:  {array}")    
    result = [i for i in range(len(array)) if lower_limit < array[i] < upper_limit]
    print(f"Индексы элементов, которые больше {lower_limit} и меньше {upper_limit}: {result}")

main()
