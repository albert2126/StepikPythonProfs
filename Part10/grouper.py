"""
Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные в кортежи
 по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей, то ими
 становится значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном
порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию grouper(), но не код,
 вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.
"""

from typing import Iterable, Iterator
# from itertools import


def grouper(it: Iterable, n: int) -> Iterator[tuple]:
    itr = iter(it)
    grp, cur = tuple(), next(itr, None)
    while cur is not None:
        if len(grp) < n:
            grp += tuple((cur,))
        else:
            yield grp
            grp = (cur,)
        cur = next(itr, None)
    if 1 < len(grp):
        grp += (None,) * (n - len(grp))
        yield grp


# Tests:
numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))

iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))
