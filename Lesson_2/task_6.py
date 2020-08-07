"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random

greeting = print('***** Игра: Угадай число ***** \n')
random_number = random.randint(0, 100)


def func_user_number():
    return int(input('Угадай число от 0 до 100 : '))


def guess_the_number(random_number, user_number, count=1):
    if count < 10:
        if user_number > random_number:
            print('Загаданное число меньше.')
            return guess_the_number(random_number, func_user_number(), count + 1)
        elif user_number < random_number:
            print('Загаданное число больше.')
            return guess_the_number(random_number, func_user_number(), count + 1)
        else:
            return 'Поздравляю, Вы угадали.'
    elif count == 10 and user_number == random_number:
        return 'Поздравляю, Вы угадали.'
    else:
        return (f'Вы проиграли. Загаданное число: {random_number}')


print(guess_the_number(random_number, func_user_number()))
