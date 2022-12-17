from zipfile import ZipFile
with ZipFile('workbook.zip') as zf:
    print(sum([1 for f in zf.infolist() if not f.is_dir()]))
