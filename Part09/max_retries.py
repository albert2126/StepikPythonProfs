import functools


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decorator(func):
        count = times
        print(count)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            while count:
                print(count)
                try:
                    val = func(*args, **kwargs)
                    return val
                except Exception:
                    count -= 1
            raise MaxRetriesException
        return wrapper
    return decorator


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()


from time import p