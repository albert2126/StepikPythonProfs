from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zf:
        if not args:
            zf.extractall()
        else:
            [zf.extract(f) for f in args]
