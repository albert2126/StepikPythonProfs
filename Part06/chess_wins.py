from collections import defaultdict


def wins(games):
    winners = defaultdict(set)
    for w, l in games:
        winners[w].add(l)
    return winners


# Tests:
# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))
#
# result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))

result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
