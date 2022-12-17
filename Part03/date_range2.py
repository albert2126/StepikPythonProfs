from datetime import date
import calendar


def get_days_in_month(y, month):
    m = list(calendar.month_name).index(month)
    return [date(y, m, d) for d in range(1, calendar.monthrange(int(y), m)[1] + 1)]


print(get_days_in_month(2021, 'December'))
