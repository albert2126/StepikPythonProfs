n = int(input())
languages = set(input().split(', '))
for _ in range(n - 1):
    languages = languages.intersection(set(input().split(', ')))
if not languages:
    print("Сериал снять не удастся")
else:
    print(*sorted(languages), sep=', ')
