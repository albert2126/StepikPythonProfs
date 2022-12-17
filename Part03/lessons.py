from datetime import datetime, timedelta
pattern = '%H:%M'
start, end = (datetime.strptime(input(), pattern) for _ in range(2))
total = ((end - start).seconds + 600) // (55 * 60)
[print(f"{(start + timedelta(minutes=55 * i)).strftime(pattern)} - "
       f"{(start + timedelta(minutes=45 + 55 * i)).strftime(pattern)}") for i in range(total)]
