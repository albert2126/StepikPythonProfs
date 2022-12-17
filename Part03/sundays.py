from datetime import date, datetime


def num_of_sundays(y):
    return len(list(filter(lambda x: datetime.fromordinal(x).weekday() == 6,
                           range(date(y, 1, 1).toordinal(), date(y+1, 1, 1).toordinal()))))


print(num_of_sundays(2021))
print(num_of_sundays(2000))
print(num_of_sundays(768))
