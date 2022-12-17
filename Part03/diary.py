from datetime import datetime

with open('diary.txt', encoding='utf-8') as fd:
    text = fd.readlines()

records, i = [[]], 0
for line in text:
    if line == '\n':
        i += 1
        records += [[]]
    else:
        records[i] += [line.strip()]
srecords = sorted(records, key=lambda x: datetime.strptime(x[0].strip(), '%d.%m.%Y; %H:%M'))
for record in srecords:
    print(*record, sep='\n')
    print()

# with open('diary.txt', encoding='utf-8') as f:
#     data = f.read().split('\n\n')
#     print('\n\n'.join(sorted(data, key=lambda x: datetime.strptime(x[: 17], '%d.%m.%Y; %H:%M'))))

