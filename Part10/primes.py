from math import sqrt
from typing import Generator


def primes(left: int, right: int) -> Generator[int]:
    if left <= 2 <= right:
        yield 2
    left = max(3, left + (left + 1) % 2)
    for i in range(left, right + 1, 2):
        if all(i % n for n in range(3, int(sqrt(i) + 1), 2)):
            yield i


