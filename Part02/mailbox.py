import re

name_pattern = re.compile(r"([a-z]+-[a-z]+)")
name_number_pattern = re.compile(r"([a-z]+-[a-z]+)(\d*)")
mboxes = {}

for _ in range(int(input())):
    name, nb = name_number_pattern.match(input()).groups()
    number = 0 if nb == '' else int(nb)
    mboxes[name] = mboxes.get(name, []) + [number]

for _ in range(int(input())):
    name, number = name_pattern.match(input()).group(1), 0
    if name in mboxes:
        numbers = mboxes[name]
        number = max(numbers) + 1
        for i in range(max(numbers)):
            if i not in numbers:
                number = i
                break
    mboxes[name] = mboxes.get(name, []) + [number]
    number = '' if number == 0 else str(number)
    print(f"{name}{number}@beegeek.bzz")
