from typing import Any, Generator, Iterable


def unique(itr: Iterable) -> Generator[Any, None, None]:
    past = []
    for v in itr:
        if (v, type(v)) not in past:
            past.append((v,type(v)))
            yield v


# Tests:
# numbers = [1, 2, 2, 3, 4, 5, 5, 5]
# print(*unique(numbers))
#
# iterator = iter('111222333')
# uniques = unique(iterator)
# print(next(uniques))
# print(next(uniques))
# print(next(uniques))

sequence = (1, [1,2], 3, [1,2], 4)
print(*unique(sequence))

sequence = (1, [1, 2], 3, [1, 2], 4, 0, 1.0, 1, True, True, False, 0)
print(*unique(sequence))
