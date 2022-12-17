import csv

with open('prices.csv', encoding='utf-8') as fd:
    rows = list(csv.DictReader(fd, delimiter=';'))

cheapest_by_shop = {r['Магазин']: min([prod for prod in r.items() if prod[0] != 'Магазин'], key=lambda x: int(x[1]))
                    for r in rows}
cheapest = min(cheapest_by_shop.items(), key=lambda p: (int(p[1][1]), p[1][0], p[0]))

print(f"{cheapest[1][0]}: {cheapest[0]}")
