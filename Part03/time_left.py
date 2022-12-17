from datetime import datetime as dt
PATTERN, RELEASE = '%d.%m.%Y %H:%M', dt(2022, 11, 8, 12, 0)
day_decl, hour_decl, min_decl = ("день", "дня", "дней"), ("час", "часа", "часов"), ("минута", "минуты", "минут")


def choose_plural(amount, declensions):
    decl = declensions[0] if amount % 100 == 1 or amount % 10 == 1 and amount % 100 > 20 \
        else declensions[1] if 1 < amount % 100 < 5 or 1 < amount % 10 < 5 and amount % 100 > 20 \
        else declensions[2]
    return str(amount) + ' ' + decl


today = dt.strptime(input(), PATTERN)
if today >= RELEASE:
    text = "Курс уже вышел!"
else:
    left = RELEASE - today
    fmt = (left.days, left.seconds // 3600, left.seconds % 3600 // 60)
    if fmt[0] > 0:
        if fmt[1] > 0:
            text = f"До выхода курса осталось: {choose_plural(fmt[0], day_decl)} и {choose_plural(fmt[1], hour_decl)}"
        else:
            text = f"До выхода курса осталось: {choose_plural(fmt[0], day_decl)}"
    else:
        if fmt[1] > 0:
            if fmt[2] > 0:
                text = f"До выхода курса осталось: {choose_plural(fmt[1], hour_decl)} и {choose_plural(fmt[2], min_decl)}"
            else:
                text = f"До выхода курса осталось: {choose_plural(fmt[1], hour_decl)}"
        else:
            text = f"До выхода курса осталось: {choose_plural(fmt[2], min_decl)}"
print(text)
