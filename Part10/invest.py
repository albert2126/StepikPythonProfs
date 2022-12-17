with open('data.csv', encoding='utf-8') as fd:
    lines = (line.strip().split(',') for line in fd)
    next(lines)
    print(sum(int(money) for _, money, rnd in lines if rnd == 'a'))


