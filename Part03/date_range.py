from datetime import date

def get_date_range(start, end):
   if start > end: return []
   else:
        ords, orde = start.toordinal(), end.toordinal()
        return [date.fromordinal(d) for d in range(ords, orde + 1)]

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))
