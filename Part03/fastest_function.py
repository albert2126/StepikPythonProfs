import time


def duration(f, arg):
    t1 = time.perf_counter()
    f(arg)
    return time.perf_counter() - t1


def duration1(f):
    t1 = time.perf_counter()
    res = f()
    return time.perf_counter() - t1


def get_the_fastest_func(funcs, arg):
    func = funcs[0]
    min_time = duration(func, arg)
    for f in funcs:
        ftime = duration(f, arg)
        if ftime < min_time:
            min_time = ftime
            func = f
    return func


def get_the_fastest_func1(funcs):
    func = funcs[0]
    min_time = duration1(func)
    for f in funcs:
        ftime = duration1(f)
        if ftime < min_time:
            min_time = ftime
            func = f
    return func


def add(a):
    for i in range(1000):
        a + a


def mult(a):
    for i in range(1000):
        a * a


from math import factorial                   # функция из модуля math


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(1000)))
