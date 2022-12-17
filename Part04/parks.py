import csv, json
parks = {}
with open('playgrounds.csv') as ifd, open('addresses.json', 'w', encoding='utf-8') as ofd:
    for row in csv.DictReader(ifd, delimiter=';'):
        adm, reg = row['AdmArea'], row['District']
        if adm not in parks:
            parks[adm] = {}
        parks[adm][reg] = parks[adm].get(reg, []) + [row['Address']]
    json.dump(parks, ofd, indent=3, ensure_ascii=False)
