import csv


def csv_columns(file_name):
    cols = {}
    with open(file_name) as fd:
        rows = list(csv.reader(fd))
    headers = rows[0]
    for i in range(len(headers)):
        cols[headers[i]] = [row[i] for row in rows[1:]]
    return cols


print(csv_columns('test_csv_columns.csv'))
