from csv import DictReader
from collections import Counter

with open('name_log.csv') as fd:
    counter = Counter(map(lambda line: line['email'], DictReader(fd)))

[print(f"{email}: {cnt}") for email, cnt in sorted(counter.items())]
