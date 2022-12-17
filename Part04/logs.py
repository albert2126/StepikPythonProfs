import csv
from datetime import datetime as dt

pattern = '%d/%m/%Y %H:%M'
users = {}
with open('name_log.csv') as ifd:
    for r in csv.DictReader(ifd):
        users[r['email']] = users.get(r['email'], []) + [(r['username'], dt.strptime(r['dtime'], pattern))]

latest = sorted([(email, max(val, key=lambda x: x[1])) for email, val in users.items()], key=lambda x: x[0])
with open('new_name_log.csv', 'w') as ofd:
    writer = csv.writer(ofd)
    writer.writerow(['username', 'email', 'dtime'])
    writer.writerows([[y[0], x, dt.strftime(y[1], pattern)] for x, y in latest])
# [print(f"{y[0]},{x},{dt.strftime(y[1], pattern)}") for x, y in latest[:10]]
