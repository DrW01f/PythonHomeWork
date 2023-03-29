# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть

def InputFunc():
    count = int(input("Введите кол-во монеток: "))
    monets = []
    for i in range(0, count):
        monets.append(int(input("Введите 1 (решка) или 0 (орел):  ")))
    print(monets)
    return monets


def Calculation(tuple):
    zeroCount = 0
    oneCount = 0
    for i in range(0, len(tuple)):
        if tuple[i] == 0:
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        result = oneCount
    else:
        result = zeroCount
    print(f"Нужно перевернуть {result} монет(ы)")


def Main():
    input = InputFunc()
    Calculation(input)


Main()
