import re, sys
text = sys.stdin.read()
print(re.sub(r'(^\W*?""".*?"""\n)|^#.*?\n|^\W{2,}#.*?\n|#.*?$', r'', text, flags=re.M | re.S))


print(re.sub(r'^\W*?""".*?"""\n|^#.*?\n|^\W*#.*?\n|(\w+\W*)#.*?$', r'\1', text, flags=re.M | re.S))

re.compile()