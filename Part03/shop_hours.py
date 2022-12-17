from datetime import datetime as dt

opened = [(dt.strptime('9', '%H'), dt.strptime('21', '%H')) for _ in range(5)] + \
       [(dt.strptime('10', '%H'), dt.strptime('18', '%H'))] * 2
inp = input().split()
wd, t = dt.strptime(inp[0], '%d.%m.%Y').weekday(), dt.strptime(inp[1], '%H:%M')
print((opened[wd][1] - t).seconds // 60 if opened[wd][0] <= t < opened[wd][1] else "Магазин не работает")
