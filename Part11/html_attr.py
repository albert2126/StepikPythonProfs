import re, sys

element, attribute, eldict = r'<(\w+)(.*?)>', r'(\w+)=', {}
for line in sys.stdin:
    elements = re.findall(element, line)
    for tag, attrs in elements:
        eldict.setdefault(tag, set()).update(set(re.findall(attribute, attrs)))
for key in sorted(eldict):
    print(key + ':', *sorted(eldict[key]))
