from datetime import datetime
pattern = '%d.%m.%Y'


def fill_up_missing_dates(dates):
    ords = sorted([datetime.strptime(d, pattern).toordinal() for d in dates])
    return [datetime.fromordinal(d).strftime(pattern) for d in range(ords[0], ords[-1] + 1)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))
