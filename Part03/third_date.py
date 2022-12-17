from datetime import datetime as dt, timedelta as td
pattern = '%d.%m.%Y'

start, end = (dt.strptime(inp, pattern) for inp in (input(), input()))
delta = td(days=1)
dat = start if (start.day + start.month) % 2 \
    else start + delta if ((start + delta).day + (start + delta).month) % 2 \
    else start + delta * 2
while dat <= end:
    if dat.weekday() not in (0, 3):
        print(dat.strftime(pattern))
    dat += delta * 3
