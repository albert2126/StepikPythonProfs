import json, sys
for key, value in json.loads(sys.stdin.read()).items():
    if type(value) == list:
        print(f"{key}: {', '.join(map(str, value))}")
    else:
        print(f"{key}: {value}")
