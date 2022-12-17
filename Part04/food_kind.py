import json
srvs = {}
with open('food_services.json') as fd:
    for srv in json.load(fd):
        tp, name, seats = srv['TypeObject'], srv['Name'], srv['SeatsCount']
        srvs[tp] = srvs.get(tp, []) + [(name, seats)]

[print(f"{key}: {val[0]}, {val[1]}") for key, val in sorted([(k, max(v, key=lambda x: x[1])) for k, v in srvs.items()])]
