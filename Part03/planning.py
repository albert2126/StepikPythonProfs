from datetime import datetime
pattern = '%d.%m.%Y'
dates, n = [datetime.strptime(input(), pattern).toordinal()], 1
for i in range(1, 10):
    n += 1
    dates += [dates[i - 1] + n]
print(*[datetime.fromordinal(d).strftime(pattern) for d in dates], sep='\n')
