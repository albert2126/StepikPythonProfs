from typing import Generator, Iterable


def pairwise(it: Iterable) -> Generator[tuple, None, None]:
    itr, nxt = iter(it), None
    # print(*itr)
    try:
        current = next(itr)
    except StopIteration:
        return
    while True:
        try:
            nxt = next(itr)
        except StopIteration:
            nxt = None
            break
        yield current, nxt
        print(current, nxt)
        current = nxt
    yield current, nxt


# Tests:
data = map(abs, range(-3, 3))
print(*pairwise(data))