"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

a=[i for i in range(1000)]
print(timeit("func_1(a)","from __main__ import func_1, a", number=50000))

def func_2(nums):
    new_arr =[i for i in range(len(nums)) if i%2==0]
    return new_arr

b=[i for i in range(1000)]
print(timeit("func_2(b)","from __main__ import func_2, b", number=50000))


def func_3(nums):
    new_arr =list(range(0,len(nums),2))
    return new_arr

c=[i for i in range(1000)]
print(timeit("func_3(c)","from __main__ import func_3, c", number=50000))


"""
После первой оптимизации кода понял, что осталась линейная сложность, попробовал вставить range для изменения
на константную. Удивился полученным результатам. Разница между первой и последней функцией в 10 раз. 
"""