import csv

col = int(input())
with open('deniro.csv') as fd:
    rows = list(csv.reader(fd))
is_digit = rows[0][col - 1].isdigit()
[print(*row, sep=',') for row in sorted(rows, key=lambda r: int(r[col - 1]) if is_digit else r[col - 1])[:10]]
