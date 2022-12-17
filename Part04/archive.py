from zipfile import ZipFile


def conv(bytes):
    units = ['B', 'KB', 'MB', 'GB']
    val, unit = bytes, 0
    while val > 1023:
        val = round(val / 1024)
        unit += 1
    return f"{val} {units[unit]}"


with ZipFile('desktop.zip') as zf:
    files = zf.infolist()
for f in files:
    indent = '  ' * f.filename.rstrip('/').count('/')
    name = f.filename.rstrip('/').split('/')[-1]
    size = '' if f.is_dir() else ' ' + conv(f.file_size)
    print(indent + name + size)
