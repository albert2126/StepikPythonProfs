def spell(*args):
    rep = {}
    for arg in args:
        arg = arg.lower()
        if not arg[0] in rep or len(arg) > rep[arg[0]]:
            rep[arg[0]] = len(arg)
    return rep


print(spell('россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН'))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
print(spell('fruit', 'football', 'February', 'forest', 'Family'))
print(spell())
