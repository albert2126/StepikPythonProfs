from string import ascii_lowercase
from itertools import product

letters = ascii_lowercase[:8]
digits = [1, 2, 3, 4, 5, 6, 7, 8]

print(*(f"{i[0]}{i[1]}" for i in product(letters, digits)))
# for letter in letters:
#     for digit in digits:
#         print(letter, digit, sep='', end=' ')

