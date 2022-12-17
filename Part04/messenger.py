import sys
p_all = [p.strip().split(' / ') for p in sys.stdin]
[print(p[0]) for p in sorted(list(sorted([p for p in p_all[:len(p_all) - 1] if p[1] == p_all[-1][0]],
                                         key=lambda a: a[0])), key=lambda b: b[2])]
# [print(p[0]) for p in posts]
