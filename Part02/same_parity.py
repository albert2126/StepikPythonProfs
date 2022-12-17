def same_parity(numbers):
    return [i for i in numbers if i % 2 == numbers[0] % 2]

print(same_parity([6, 1, 4, -13, -20, 42]))
