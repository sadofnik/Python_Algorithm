"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# i = int(input('Введите порядковый номер искомого простого числа: '))
# i = 100
# print(simple(i))


def resheto(c):
    """С использованием «Решета Эратосфена»"""
    a = [i for i in range(2, 10000)]
    count = 0
    for i in a:
        if count < c:
            if i != 0:
                count += 1
                for j in range(a.index(i) + i, len(a), i):
                    a[j] = 0
    a = set(a)
    a.remove(0)
    a = sorted(list(a))
    return a[c-1]


# user_input = int(input('Введите порядковый номер искомого простого числа: '))
# user_input = 100
# print(resheto(user_input))

print(timeit("simple(10)", "from __main__ import simple", number=100)) # 0.0039
print(timeit("resheto(10)", "from __main__ import resheto", number=100)) # 0.2771
print(timeit("simple(100)", "from __main__ import simple", number=100)) # 0.4324
print(timeit("resheto(100)", "from __main__ import resheto", number=100)) # 0.3837
print(timeit("simple(1000)", "from __main__ import simple", number=100)) # 91.2836
print(timeit("resheto(1000)", "from __main__ import resheto", number=100)) # 9.4675

"""
При увеличении входных данных решение при помощи "Решета Эратосфена" даёт результат
в несколько раз лучше, чем обычный метод, хотя при маленьких значениях данный метод немного отстаёт.
"""