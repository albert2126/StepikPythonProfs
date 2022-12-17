import sys
from datetime import datetime as dt
ptn = '%d.%m.%Y'

days = [dt.strptime(d.strip(), ptn) for d in sys.stdin]
rule = days[0] < days[1]
print(type(rule), rule)
direction = 'MIX'
for i in range(len(days) - 1):
    if days[i + 1] > days[i]:
        if direction == 'MIX':
            direction = 'ASC'
        elif direction == 'DESC':
            direction = 'MIX'
            break
    elif days[i + 1] < days[i]:
        if direction == 'MIX':
            direction = 'DESC'
        elif direction == 'ASC':
            direction = 'MIX'
            break
    else:
        direction = 'MIX'
        break

print(direction)