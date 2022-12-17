def choose_plural(amount, declensions):
    decl = declensions[0] if amount % 100 == 1 or amount % 10 == 1 and amount % 100 > 20 \
        else declensions[1] if 1 < amount % 100 < 5 or 1 < amount % 10 < 5 and amount % 100 > 20 \
        else declensions[2]
    return str(amount) + ' ' + decl

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))

print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
