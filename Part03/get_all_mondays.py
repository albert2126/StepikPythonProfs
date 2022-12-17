from datetime import date, timedelta
import calendar


def get_all_mondays(y):
    res, mon = [], date(y, 1, 1 + (7 - calendar.weekday(y, 1, 1)) % 7)
    while mon <= date(y, 12, 31):
        res += [mon]
        mon += timedelta(days=7)
    return res


print(get_all_mondays(2021))
