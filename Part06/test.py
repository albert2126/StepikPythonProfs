import math
from copy import copy
from datetime import date

patterns = {'br': '%d/%m/%Y', 'ca': '%Y-%m-%d', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y', 'ru': '%d.%m.%Y', 'us': '%m-%d-%Y',}


def date_formatter(country_code):
    def intern(dt):
        return dt.strftime(patterns[country_code])
    return intern


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

n =12.3

math.floor(n)

it = iter([1,2,3])

it1 = copy(it)
