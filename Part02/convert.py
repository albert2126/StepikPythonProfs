def convert(string):
    lower_case = len([a for a in string if a.islower()]) >= len([a for a in string if a.isupper()])
    return string.lower() if lower_case else string.upper()

print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
