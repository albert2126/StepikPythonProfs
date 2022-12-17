from typing import Any, Generator, Iterable


def stop_on(itr: Iterable, obj: Any) -> Generator:
    for item in itr:
        if item == obj:
            break
        yield item


# Tests:
numbers = [1, 2, 3, 4, 5]
print(*stop_on(numbers, 4))
