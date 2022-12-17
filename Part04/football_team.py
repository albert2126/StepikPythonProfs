import json
from zipfile import ZipFile
FOLDER = 'football/'


def is_correct_json(data):
    try:
        s = json.load(open(FOLDER + data))
        return True
    except:
        return False


with ZipFile('data.zip') as zf:
    files = [f.filename for f in zf.infolist() if f.filename.endswith('.json')]
    zf.extractall(members=files, path=FOLDER)

jsfiles = filter(is_correct_json, files)
team = [f"{d['first_name']} {d['last_name']}" for d in [json.load(open(FOLDER + f)) for f in jsfiles] if d['team'] == 'Arsenal']
print(*(sorted(team)), sep='\n')

