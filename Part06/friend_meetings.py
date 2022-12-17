import csv
from collections import namedtuple
from datetime import datetime as dt

Friend = namedtuple('Friend', {'surname': '', 'name': '', 'meeting_date': '', 'meeting_time': ''})
with open('meetings.csv') as fd:
    friends = tuple(Friend(*f.values()) for f in csv.DictReader(fd))

sort_friends = sorted(friends, key=lambda f: dt.strptime(f"{f.meeting_date} {f.meeting_time}", '%d.%m.%Y %H:%M'))
[print(f"{f.surname} {f.name}") for f in sort_friends]
