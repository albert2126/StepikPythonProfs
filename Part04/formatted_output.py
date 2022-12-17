from zipfile import ZipFile
from datetime import datetime as dt
with ZipFile('workbook.zip') as zf:
    for file in sorted([(f.filename.rsplit('/', 1)[-1], dt(*f.date_time), f.file_size, f.compress_size) for f in zf.infolist() if not f.is_dir()]):
        print(file[0])
        print(f"  Дата модификации файла: {file[1]}")
        print(f"  Объем исходного файла: {file[2]} байт(а)")
        print(f"  Объем сжатого файла: {file[3]} байт(а)\n")
