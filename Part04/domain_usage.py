import csv

with open('data.csv') as ifd:
    domains = {}
    rows = csv.reader(ifd)
    for row in list(rows)[1:]:
        domain = row[2].split('@')[1]
        domains[domain] = domains.get(domain, 0) + 1
        d_alpha = [(d, domains[d]) for d in list(sorted(domains))]
        d_sorted = list(sorted(d_alpha, key=lambda x: x[1]))
    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as ofd:
        writer = csv.writer(ofd)
        writer.writerow(['domain', 'count'])
        writer.writerows(d_sorted)


issubclass()