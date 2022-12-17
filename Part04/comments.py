import sys, re

comment = re.compile('[ ]*#')
print(len(list(filter(lambda x: comment.match(x), sys.stdin))))
