from functools import cmp_to_key


def compare(a, b):
    return int(a + b) - int(b + a)


def get_biggest(numbers):
    if not numbers:
        return -1
    number_str = sorted([str(n) for n in numbers])
    return int(''.join(sorted(number_str, key=cmp_to_key(compare), reverse=True)))

print(get_biggest([0,0,0,0,0]))
print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([]))

print(get_biggest(['998', '9686', '9842', '9721', '9603', '9811', '9719', '9845', '9627', '9859', '9705', '9784', '9662', '9622', '9926', '9777', '9866', '9811', '96', '9664', '9766', '9788', '9826', '9745', '9693', '9880', '9621', '96', '9671', '975', '9623']))
print(9989926988098669859984598429826981198119788978497779766975974597219719970596969693968696719664966296279623962296219603)

print(get_biggest([64, 643, 645]))
print(get_biggest([72, 7274]))
