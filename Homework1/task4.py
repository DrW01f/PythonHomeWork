# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и
# Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

def Input():
    while True:
        # без проверки на ввод числа .isdigit()
        inputCount = int(input("Введите общее количество журавликов: "))
        if inputCount > 0:
            break
    if inputCount % 6 != 0:
        print("Условия неверны, но пускай будут два с половиной землекопа... ")
    return inputCount


def Calculation(count):
    return count / 6


def Main():
    count = Input()
    result = Calculation(count)
    print(str(result) + " " + str(result*2) + " " + str(result))


Main()
