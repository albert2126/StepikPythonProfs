import json
with open('data1.json') as ifd1, open('data2.json') as ifd2, open('data_merge.json', 'w', encoding='utf-8') as ofd:
    json.dump(json.load(ifd1) | json.load(ifd2), ofd, indent='   ')
