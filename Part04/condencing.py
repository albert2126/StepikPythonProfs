import csv


def condense_csv(file_name, id_name):
    with open(file_name, encoding='utf-8') as ifd:
        rows = list(csv.reader(ifd))

    cols = [id_name] + [r[1] for r in rows if r[0] == rows[0][0]]
    cn = len(cols)  # 2
    rn = len(rows) // (cn - 1)  # 2
    condensed = [[rows[i * (cn - 1)][0]] + ['' for _ in range(cn - 1)] for i in range(rn)]
    for i in range(rn):
        for j in range(cn - 1):
            condensed[i][j + 1] = rows[i * (cn - 1) + j][2]

    with open('condensed.csv', 'w', encoding='utf-8') as ofd:
        writer = csv.writer(ofd)
        writer.writerow(cols)
        writer.writerows(condensed)
    return [cols] + condensed


text = '''01,Title,Ran So Hard the Sun Went Down
02,Title,Honky Tonk Heroes (Like Me)'''

with open('data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('data.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())
