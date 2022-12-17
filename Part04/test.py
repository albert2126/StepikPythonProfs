import csv


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        objects = {}
        for obj, attr, value in csv.reader(file):
            if obj not in objects:
                objects[obj] = {id_name: obj}
            objects[obj][attr] = value
        print(objects)

    with open('condensed.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=objects[obj])
        print(f"obj: {obj}; objects[obj]: {objects[obj]}")
        writer.writeheader()
        writer.writerows(objects.values())


condense_csv('data.csv', id_name='ID')
