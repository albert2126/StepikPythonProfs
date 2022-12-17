class CardDeck:

    def __init__(self):
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
        self.suit = ["пик", "треф", "бубен", "червей"]
        self.rl = len(self.rank)
        self.sl = len(self.suit)
        self.cards = [f"{self.rank[index % self.rl]} {self.suit[index // self.rl]}" for index in range(52)]
        self.limit = self.rl * self.sl
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.limit - 1:
            raise StopIteration
        self.index += 1
        return self.cards[self.index]

### Test 1 ###
# cards = CardDeck()
#
# print(next(cards))
# print(next(cards))

### Test 2 ###
cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
