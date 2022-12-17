from typing import Generator


def card_deck(suit: "str") -> Generator[str, None, None]:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    suits = ["пик", "треф", "бубен", "червей"]
    rl, sindex = len(ranks), suits.index(suit)
    cards = [f"{ranks[i % rl]} {suits[i // rl]}" for i in range(52) if i // rl != sindex]
    print(cards)
    print(len(cards))
    for card in cards:
        yield card


# Tests

# generator = card_deck('пик')
# print(next(generator))
# print(next(generator))
# print(next(generator))

generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]
print(*cards)
