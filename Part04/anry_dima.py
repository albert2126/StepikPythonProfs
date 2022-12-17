import sys

l = list(sys.stdin.readlines())
print(['Анри', 'Дима'][(len(l)) % 2 == int(l[-1]) % 2])
