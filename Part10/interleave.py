from typing import Any, Generator, Sequence


def interleave(*args: Sequence) -> Generator[Any, None, None]:
    return (item for grp in zip(*map(list, args)) for item in grp)


print(*interleave('bee', '123'))
