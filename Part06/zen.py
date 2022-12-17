from collections import Counter

with open('pythonzen.txt') as fd:
    text = Counter((ch.lower() for ch in fd.read() if ch.isalpha()))
[print(f"{ch}: {cnt}") for ch, cnt in sorted(text.items())]
