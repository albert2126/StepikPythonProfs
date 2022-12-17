def print_given(*args, **kwargs):
    [print(arg, type(arg)) for arg in args]
    [print(key, word, type(word)) for key, word in sorted(kwargs.items())]


print_given(1, [1, 2, 3], 'three', two=2)
print_given('apple', 'cherry', 'watermelon')
print_given(b=2, d=4, c=3, a=1)
