from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.printdir()
    info = zip_file.infolist()

print(*info, sep='\n')
