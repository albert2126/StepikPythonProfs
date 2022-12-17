import csv

with open('titanic.csv', encoding='utf-8') as fd:
    survived = {r['name']: r['sex'] for r in csv.DictReader(fd, delimiter=';')
                if r['survived'] == '1' and float(r['age']) < 18}

[print(name) for name, _ in sorted(survived.items(), key=lambda x: x[1], reverse=True)]
