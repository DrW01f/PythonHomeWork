# Задача 26:  Напишите программу, которая на вход принимает два числа A и
# B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def Exponentiation(number: int, degree: int):
    if degree == 0:
        return 1
    elif degree == 1:
        return number
    # print(Exponentiation(number, degree - 1) * number)
    return Exponentiation(number, degree - 1) * number


def Main():
    number = int(input("Введите число:  "))
    degree = int(input("Введите степегь числа:  "))
    result = Exponentiation(number, degree)
    print(result)


Main()
