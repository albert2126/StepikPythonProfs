word = input()
vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
positions = [i for i in range(len(word)) if word[i] in vowels]
for j in range(int(input())):
    w = input()
    if positions == [i for i in range(len(w)) if w[i] in vowels]:
        print(w)
