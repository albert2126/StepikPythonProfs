from datetime import datetime as dt
pattern = '%d.%m.%Y'

employees = []
for _ in range(int(input())):
    e = input().split()
    employees += [(dt.strptime(e[2], pattern), e[0], e[1])]
oldest = min(employees)
on = len(list(filter(lambda x: x[0] == oldest[0], employees)))
print(f"{oldest[0].strftime(pattern)} {oldest[1]} {oldest[2]}" if on == 1
      else f"{oldest[0].strftime(pattern)} {on}")
