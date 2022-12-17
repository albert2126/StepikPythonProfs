import csv

with open('sales.csv', 'r', encoding='UTF-8') as fd:
    [print(row[0]) for row in list(csv.reader(fd, delimiter=';'))[1:] if int(row[1]) > int(row[2])]
