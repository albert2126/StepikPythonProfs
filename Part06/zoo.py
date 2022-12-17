import json
from collections import Counter

with open('zoo.json') as fd:
    # ans = json.load(fd)
    print(sum(Counter(a).total() for a in json.load(fd)))
