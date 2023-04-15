# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять из одного слова, если во 
# фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг 
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с 
# клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в 
# порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  


def input_msg()->bool:
    
    msg_list = input("Введите кричалку: ").strip().split(' ')
    vowels = 'аеиоуыэюя'
    result = [] # для записи кол-ва гласных во фразе
    count = 0 
    for word in msg_list:
        for char in word:
            if char in vowels:
                count += 1
        result.append(count)
        count = 0
    print(result)
    return set(result) == 1 # если кол-во слогов было одинаковым, то 1

def result_answer():

    pass


def main():
    msg = input_msg()
    pass

main()