from datetime import datetime as dt
pattern = '%d.%m.%Y'

bds = [dt.strptime(input().split()[2], pattern) for _ in range(int(input()))]
occ = sorted(sorted([(d, bds.count(d)) for d in set(bds)], key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
i = 0
while i < len(occ) and occ[i][1] == occ[0][1]:
    print(occ[i][0].strftime(pattern))
    i += 1
