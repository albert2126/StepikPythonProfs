units = ['B', 'KB', 'MB', 'GB']
extensions = {}
with open('test_files.txt', encoding="utf-8") as fd:
    for line in fd.readlines():
        name, size, unit = line.strip().split(' ')
        ext = name.split('.')[1]
        extensions[ext] = extensions.get(ext, []) + [(name, int(size), unit)]

for ext in sorted(extensions.keys()):
    files, sum = sorted(extensions[ext]), 0
    unit = min([units.index(file[2]) for file in files])
    for file in files:
        print(file[0])
        sum += file[1] * 1024 ** (units.index(file[2]) - unit)
    while sum > 1023:
        sum = round(sum / 1024)
        unit += 1
    print("----------")
    print(f"Summary: {sum} {units[unit]}\n")
