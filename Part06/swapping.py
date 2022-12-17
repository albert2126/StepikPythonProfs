from collections import defaultdict


def flip_dict(inpdict):
    outdict = defaultdict(list)
    for k, lst in inpdict.items():
        [outdict[e].append(k) for e in lst]
    outdict.default_factory = list
    return outdict


# Tests:
print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')

data = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c', 'c'], 3: ['c', 'd', 'a'], 4: ['a', 'b', 'r', 'f'], 5: ['y', 'u', 'e', 'w']}
print(flip_dict(data))
