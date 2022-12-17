from zipfile import ZipFile
with ZipFile('workbook.zip') as zf:
    print(min([(f.filename, f.compress_size / f.file_size if f.file_size != 0 else 1)
               for f in zf.infolist()], key=lambda x: x[1])[0].split('/', 1)[1])
