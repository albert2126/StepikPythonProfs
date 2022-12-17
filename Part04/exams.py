import csv, json
from datetime import datetime as dt
PTRN = '%Y-%m-%d %H:%M:%S'

exams_all = {}
with open('exam_results.csv') as ifd, open('best_scores.json', 'w') as ofd:
    for e in csv.DictReader(ifd):
        mail, name, surn, score, date_time = e['email'], e['name'], e['surname'], int(e['score']), \
                                             dt.strptime(e['date_and_time'], PTRN)
        exams_all.setdefault(mail, []).append((name, surn, score, date_time))
    exams_final = sorted(map(lambda c: (c[0], max(c[1], key=lambda x: (x[2], x[3]))), exams_all.items()))
    output = [{"name": s[1][0], "surname": s[1][1], "best_score": s[1][2],
               "date_and_time": s[1][3].strftime(PTRN), 'email': s[0]} for s in exams_final]
    json.dump(output, ofd, indent=3)
