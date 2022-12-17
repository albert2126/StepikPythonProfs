import csv

with open('student_counts.csv', encoding='utf-8') as ifd:
    reader = list(csv.DictReader(ifd))

keys = ['year'] + [f"{str(i)}-{a}" for i, a in sorted([k.split('-') for k in reader[0] if k != 'year'],
                                                      key=lambda c: (int(c[0]), c[1]))]
new_dict = [{k: r[k] for k in keys} for r in reader]

with open('sorted_student_counts.csv', 'w') as ofd:
    writer = csv.DictWriter(ofd, fieldnames=new_dict[0].keys())
    writer.writeheader()
    writer.writerows(new_dict)
