import csv

with open('wifi.csv', encoding='utf-8') as fd:
    rows = list(csv.DictReader(fd, delimiter=';', quotechar='"'))
locations = {}
for row in rows:
    loc = row['district']
    locations[loc] = locations.get(loc, 0) + int(row['number_of_access_points'])
print(*[f"{x[0]}: {x[1]}" for x in list(sorted([(key, locations[key]) for key in list(sorted(locations))],
                                               key=lambda x: x[1], reverse=True))], sep='\n')
