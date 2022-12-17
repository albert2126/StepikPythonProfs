import time


def calculate_it(func, *args):
    t1 = time.monotonic()
    res = func(*args)
    t2 = time.monotonic()
    return res, t2 - t1


def add(a,b,c):
    time.sleep(3)
    return a + b + c


print(calculate_it(add, 1, 2, 3))
