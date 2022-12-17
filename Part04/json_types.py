import json
with open('data.json', encoding='utf-8') as ifd:
    lst = json.load(ifd)
for i in range(len(lst)):
    if type(lst[i]) == str:
        lst[i] = lst[i] + '!'
    elif type(lst[i]) == int:
        lst[i] = lst[i] + 1
    elif type(lst[i]) == bool:
        lst[i] = not lst[i]
    elif type(lst[i]) == list:
        lst[i] = lst[i] * 2
    elif type(lst[i]) == dict:
        lst[i]['newkey'] = None

new_lst = list(filter(lambda x: x is not None, lst))
with open('updated_data.json', 'w', encoding='utf-8') as ofd:
    json.dump(new_lst, ofd)
