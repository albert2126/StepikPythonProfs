def filter_anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

print(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
