from collections import Counter

counter = Counter(map(len, input().split()))
[print(f"Слов длины {length}: {cnt}") for length, cnt in sorted(counter.items(), key=lambda x: x[1])]

