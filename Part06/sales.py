from collections import Counter
import csv, json

DIR = 'prods/'
counter = Counter()
for i in range(1, 5):
    with open(f"{DIR}quarter{i}.csv") as fd:
        counter.update({ln[0]: sum(map(int, ln[1:])) for ln in list(csv.reader(fd))[1:]})

with open(f"{DIR}prices.json") as fd:
    prices = Counter(json.load(fd))
print(sum([counter[k] * prices[k] for k in counter]))
