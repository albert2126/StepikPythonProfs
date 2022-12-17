from datetime import date as d

wdays = [x.weekday() for x in [d(y, m, 13) for m in range(1, 13) for y in range(1, 10000)]]
print(*[wdays.count(x) for x in range(7)], sep='\n')
