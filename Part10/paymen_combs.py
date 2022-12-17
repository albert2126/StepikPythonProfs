from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
wl = wallet[5:]
res = []
for n in range(4, 14):
    for comb in combinations(wl, n):
        if sum(comb) == 100:
            res.append(comb)
print(len(set(res)) + 2)


