# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она
# растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке
# растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора
# черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и
# с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое
# может собрать за один заход собирающий модуль, находясь перед некоторым
# кустом заданной во входном файле грядки.
import random


def Garden():
    gardenCount = int(input("Введите кол-во грядок:  "))
    garden = [random.randint(1, 10) for i in range(gardenCount)]
    print(f"Всего {gardenCount} грядок, которые дали {garden} ягод ")
    return garden


def Calculating(array: list):
    maxIndex = int()
    summ = 0
    for i in range(1, len(array)):
        if (array[-i] + array[-i - 1] + array[-i + 1]) > summ:
            maxIndex =  i
            summ = (array[-i] + array[-i - 1] + array[-i + 1])
        print(maxIndex, summ)
    return f"С грядки {len(array) - maxIndex + 1} можно собрать {summ} ягод"


def Main():
    array = Garden()
    answer = Calculating(array)
    print(answer)


Main()
