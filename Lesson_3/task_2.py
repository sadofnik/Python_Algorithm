"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

import hashlib

user_login = 'Alex'


def gen_hash(ul, up):
    hash_passwd = hashlib.sha256((up).encode()).hexdigest()[:32] + hashlib.sha256((ul).encode()).hexdigest()[32:]
    return hash_passwd


def check_password(up, ul, hp):
    if hp == gen_hash(ul, up):
        return 'Вы ввели правильный пароль'
    else:
        return 'Вы ввели неправильный пароль'


user_password = input('Введите пароль: ')
hash_password = gen_hash(user_login, user_password)

print(f'Созданный хеш: {hash_password}')

user_password = input('Введите пароль еще раз для проверки: ')
print(check_password(user_password, user_login, hash_password))
