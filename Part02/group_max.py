d = {}
for i in range(1, int(input()) + 1):
    dsum = sum([int(s) for s in str(i)])
    d[dsum] = d.get(dsum, 0) + 1
print(max([val for val in d.values()]))
