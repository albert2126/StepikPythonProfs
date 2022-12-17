import csv

with open('salary_data.csv', encoding='utf-8') as fd:
    orgs = {}
    for row in list(csv.DictReader(fd, delimiter=';')):
        orgs[row['company_name']] = orgs.get(row['company_name'], []) + [int(row['salary'])]
    print(*list(sorted(sorted(orgs), key=lambda org: sum(orgs[org]) / len(orgs[org]))), sep='\n')
