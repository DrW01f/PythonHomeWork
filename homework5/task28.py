# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4


def SumFunc(firstNumber: int, secondNumber: int):        
    if secondNumber == 0:
        return firstNumber
    return SumFunc(firstNumber+1, secondNumber-1)
    

def Main():
    number1 = int(input("Введите первое слагаемое:  "))
    number2 = int(input("Введите второе слагаемое:  "))
    print(SumFunc(number1, number2))


Main()