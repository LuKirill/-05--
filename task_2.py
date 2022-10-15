"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from functools import reduce
from collections import defaultdict


def calc():
    n = defaultdict(list)
    for i in range(2):
        a = input(f'Введите {i + 1} натуральное шестнадцатиричное число: ')
        n[f'{i + 1}-{a}'] = list(a)
    print(n)

    sum_res = sum([int(''.join(j), 16) for j in n.values()])
    print(sum_res)
    print('Сумма: ', list('%X' % sum_res))
    mul_res = reduce(lambda c, b: c * b, [int(''.join(j), 16) for j in n.values()])
    print('Произведение: ', list('%X' % mul_res))


calc()
