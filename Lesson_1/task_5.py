"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
"""Пример создания стека через ООП"""

from random import randint

class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


# Имитация очереди из n-элементов
list_numbers = [randint(0,50) for i in range(28)]

# Устанавливаем значение размера стека
max_value = 5

# Расчёт количества стопок
if len(list_numbers)%max_value > 0:
    sum_stack = len(list_numbers)//max_value + 1
else:
    sum_stack = len(list_numbers)//max_value

# Создаём список стопок
list_stack= []
for i in range(sum_stack):
     list_stack.append('stack_' + str(i))

# Заполняем стопки
for i in range(len(list_stack)):
    list_stack[i] = StackClass()
    if len(list_numbers) >= max_value:
        for m in range(max_value):
            list_stack[i].push_in(list_numbers[0])
            del list_numbers[0]
    else:
        for m in range(len(list_numbers)):
            list_stack[i].push_in(list_numbers[0])
            del list_numbers[0]

# Для проверки
for i in range(len(list_stack)):
    print(list_stack[i].elems)
