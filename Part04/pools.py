import json, time
PTRN = '%H:%M'
TMIN, TMAX = time.strptime('10:00', PTRN), time.strptime('12:00', PTRN)


def proper_hours(hours):
    return all(map(lambda h: TMIN >= time.strptime(h[0], PTRN) and time.strptime(h[1], PTRN) >= TMAX,
                   [hrs.split('-') for hrs in hours.values()]))


with open('pools.json') as fd:
    pool = max([(r["DimensionsSummer"]["Length"], r["DimensionsSummer"]["Width"], r["Address"]) for r in json.load(fd) if proper_hours(r["WorkingHoursSummer"])], key=lambda p: (p[0], p[1]))
print(f"{pool[0]}x{pool[1]}")
print(pool[2])
