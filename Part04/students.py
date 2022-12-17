import csv, json
with open('students.json') as ifd, open('data.csv', 'w', encoding='utf-8') as ofd:
    students = sorted([(r['name'], r['phone']) for r in json.load(ifd) if r['age'] >= 18 and r['progress'] >= 75])
    writer = csv.writer(ofd)
    writer.writerow(('name', 'phone'))
    writer.writerows(students)

print(students)
