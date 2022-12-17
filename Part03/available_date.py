from datetime import datetime
pattern = '%d.%m.%Y'


def date2ordinals(d):
    lst = d.split('-')
    if len(lst) == 1:
        return [datetime.strptime(lst[0], pattern).toordinal()]
    return list(range(datetime.strptime(lst[0], pattern).toordinal(), datetime.strptime(lst[1], pattern).toordinal() + 1))


def is_available_date(booked_dates, booking_dates):
    b = []
    for d in booked_dates:
        b += date2ordinals(d)
    booked = set(b)
    booking = set(date2ordinals(booking_dates))
    return len(booked & booking) == 0


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
