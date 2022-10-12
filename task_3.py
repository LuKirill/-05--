"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from timeit import timeit
from collections import deque

n = 10 ** 2
my_list_1 = []
my_deque_1 = deque()
my_list_2 = [n for n in range(10 ** 2)]
my_deque_2 = deque([m for m in range(10 ** 2)])


def list_pop(lst):
    lst.pop()
    return lst


def list_extend(lst):
    lst.extend(my_list_2)
    return lst


def list_append(lst):
    for i in range(n):
        lst.append(i)
    return lst


def deque_append(d):
    for i in range(n):
        d.append(i)
    return d


def deque_pop(d):
    d.pop()
    return d


def deque_extend(d):
    d.extend(my_deque_2)
    return d


def list_popleft(lst):
    lst.pop(0)
    return lst


def list_extendleft(lst):
    lst.extend(0, my_list_2)
    return lst


def list_insert(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def deque_appendleft(d):
    for i in range(n):
        d.appendleft(i)
    return d


def deque_popleft(d):
    d.popleft()
    return d


def deque_extendleft(d):
    d.extendleft(my_deque_2)
    return d


def list_get_el(lst):
    for i in lst:
        return lst[i]


def deque_get_el(d):
    for i in d:
        return d[i]


print("Cравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее")
print('Время удаления последнего элемента из списка при 10 повторениях: ',
      timeit('list_pop(my_list_2)', globals=globals(), number=10))
print('Время заполнения списка методом extend при 10 повторениях: ',
      timeit('list_extend(my_list_2)', globals=globals(), number=10))
print('Время заполнение списка методом append при 10 повторениях: ',
      timeit('list_append(my_list_1)', globals=globals(), number=10))
print()
print('Время удаления последнего элемента из двухсторонней очереди при 10 повторениях: ',
      timeit('deque_pop(my_deque_2)', globals=globals(), number=10))
print('Время заполнения методом extend двухсторонней очереди при 10 повторениях: ',
      timeit('deque_extend(my_deque_2)', globals=globals(), number=10))
print('Время заполнения двухсторонней очереди методом append при 10 повторениях: ',
      timeit('deque_append(my_deque_1)', globals=globals(), number=10))
print()
print('Cравнить операции appendleft, popleft, extendleft дека и '
      'соответствующих им операций списка и сделать выводы что и где быстрее')
print('Время удаления первого элемента из списка при 10 повторениях: ',
      timeit('list_popleft(my_list_2)', globals=globals(), number=10))
print('Время заполнения списка методом extend слева при 10 повторениях: ',
      timeit('list_extend(my_list_2)', globals=globals(), number=10))
print('Время заполнение списка методом insert при 10 повторениях: ',
      timeit('list_insert(my_list_1)', globals=globals(), number=10))
print()
print('Время удаления последнего элемента из двухсторонней очереди при 10 повторениях: ',
      timeit('deque_popleft(my_deque_2)', globals=globals(), number=10))
print('Время заполнения методом extendleft двухсторонней очереди при 10 повторениях: ',
      timeit('deque_extendleft(my_deque_2)', globals=globals(), number=10))
print('Время заполнения двухсторонней очереди методом appendleft при 10 повторениях: ',
      timeit('deque_appendleft(my_deque_1)', globals=globals(), number=10))
print()
print('сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее')
print('Время получения элемента из списка при 10 повторениях: ',
      timeit('deque_get_el(my_deque_2)', globals=globals(), number=10))
print('Время получения элемента из двухсторонней очереди при 10 повторениях: ',
      timeit('list_get_el(my_list_2)', globals=globals(), number=10))

# Если заполнение списка происходит путем вставки элемента в начало списка, то deque работает быстрее,
# тк сложность операции вставки в начало и конец О(1), для списка вставка в начало О(n)

# Метод extendleft(deque(list)) для deque работает медленней, чем extend(0, list) для списка

# В остальных проверках операции над deque проходят бытрей, чем над list