# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите
# Кате отгадать задуманные Петей числа

def InputCount():
    countXY = [0, 0]
    countXY[0] = int(input("Введите сумму чисел:  "))
    countXY[1] = int(input("Введите произведение чисел:  "))
    return countXY


def Calculation(counts):
    discriminant = counts[0]**2 - 4 * counts[1]
    if discriminant < 0:
        print("Дискриминант меньше 0, таких чисел не существует")
    else:
        Y1 = (counts[0] - discriminant ** (1/2)) / 2
        Y2 = (counts[0] + discriminant ** (1/2)) / 2
    if Y1 == Y2:
        
        print(f"Загаданные числа: {Y1} и {counts[0] - Y1}")
    else:
        print(f"Загаданные числа: {Y1} , {counts[0] - Y1} или {Y1} , {counts[0] - Y2}")


def Main():
    counts = InputCount()
    Calculation(counts)


Main()
