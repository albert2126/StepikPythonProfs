language = 0
for i in range(3):
    language |= 1 if 64 < ord(input()) < 123 else 2

print(('', 'en', 'ru', 'mix')[language])
