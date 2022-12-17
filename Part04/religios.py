import json
religions = {}
with open('countries.json') as ifd, open('religion.json', 'w', encoding='utf-8') as ofd:
    for d in json.load(ifd):
        religions[d['religion']] = religions.get(d['religion'], []) + [d['country']]
    json.dump(religions, ofd, indent=3)
