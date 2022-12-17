import json
by_district, by_net = {}, {}
with open('food_services.json') as fd:
    for srv in json.load(fd):
        dstr = srv['District']
        by_district[dstr] = by_district.get(dstr, 0) + 1
        if srv['OperatingCompany']:
            net = srv['OperatingCompany']
            by_net[net] = by_net.get(net, 0) + 1

district = max(by_district.items(), key=lambda x: x[1])
net = max(by_net.items(), key=lambda x: x[1])
print(f"{district[0]}: {district[1]}")
print(f"{net[0]}: {net[1]}")
