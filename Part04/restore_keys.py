import json

with open('people.json') as ifd:
    dicts = list(json.load(ifd))

keys = set()
for d in dicts:
    keys.update(d.keys())

for d in dicts:
    for k in keys:
        d.setdefault(k, None)

with open('updated_people.json', 'w', encoding='utf-8') as ofd:
    json.dump(dicts, ofd, indent=3)
