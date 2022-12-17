from datetime import datetime as dt, timedelta as td
p = '%d.%m.%Y'

today, maxdate = dt.strptime(input(), p), dt(1, 1, 1)
year, youngest = today.year, ("", maxdate)

for _ in range(int(input())):
    born = input().split()
    bdate = dt.strptime(born[2], p)
    if bdate > maxdate and (0 < (bdate.replace(year=year) - today).days <= 7
                            or 0 < (bdate.replace(year=year+1) - today).days <= 7):
        maxdate = bdate
        youngest = (f"{born[0]} {born[1]}", maxdate)

print(youngest[0] if youngest[0] else "Дни рождения не планируются")
