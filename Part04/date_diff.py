import sys
from datetime import datetime as dt
pattern = '%Y-%m-%d'

dates = [dt.strptime(s.strip(), pattern) for s in sys.stdin]
print((max(dates) - min(dates)).days)
