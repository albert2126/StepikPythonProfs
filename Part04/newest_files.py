from zipfile import ZipFile
from datetime import datetime as dt
PTRN = '%Y-%m-%d %H:%M:%S'
OLDEST = dt.strptime('2021-11-30 14:22:00', PTRN)
with ZipFile('workbook.zip') as zf:
    files = [f.filename.rsplit('/', 1)[-1] for f in zf.infolist() if not f.is_dir() and dt(*f.date_time) > OLDEST]
print(*sorted(files), sep='\n')
