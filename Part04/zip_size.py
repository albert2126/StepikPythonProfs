from zipfile import ZipFile
from functools import reduce

with ZipFile('workbook.zip') as zf:
    count1 = reduce(lambda x, y: x + y, [f.file_size for f in zf.infolist()])
    count2 = reduce(lambda x, y: x + y, [f.compress_size for f in zf.infolist()])
print(f"Объем исходных файлов: {count1} байт(а)")
print(f"Объем сжатых файлов: {count2} байт(а)")
