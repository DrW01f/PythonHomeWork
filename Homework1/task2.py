# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


def Input():
    while True:  # проверка на трехзначное число без проверки на ввод числа .isdigit()
        inputCount = int(input("Введите трехзначное число: "))
        if 99 < inputCount < 1000:
            return inputCount


def SumFounder(count):
    # Делит число на составные
    summ = count % 10 + count % 100 // 10 + count // 100
    return summ


def Main():
    count = Input()
    print(count)
    summ = SumFounder(count)
    print(summ)


Main()
