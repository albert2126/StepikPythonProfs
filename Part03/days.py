from datetime import datetime, timedelta
pattern = '%d.%m.%Y'
dates = [datetime.strptime(x, pattern) for x in input().split()]
diff, prev = [], dates[0]
for i in range(1, len(dates)):
    diff += [abs((dates[i] - prev).days)]
    prev = dates[i]
print(diff)
