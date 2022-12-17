import sys
for line in sys.stdin.readlines():
    print(''.join(line[-2 - i] for i in range(len(line) - 1)))

# print(sys.stdin.readlines())
