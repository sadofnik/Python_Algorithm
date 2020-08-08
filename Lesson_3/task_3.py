"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib

a = 'papa'


def f(s, b=[]):
    for i in range(len(s)):
        if len(s) == 1:
            if s[i] not in b:
                b.append(s[i])
            return b
        else:
            if s[i:] not in b:
                b.append(s[i:])
        return f(s[i + 1:]) and f(s[:len(s) - 1])


b = f(a)
b.remove(a)
print(b)

for i in range(len(b)):
    print(hashlib.md5((b[i]).encode()).hexdigest())
