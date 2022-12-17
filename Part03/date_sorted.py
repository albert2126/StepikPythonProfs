from datetime import date
input_sorted = sorted([input() for _ in range(int(input()))])
print(*[date.fromisoformat(d).strftime('%d/%m/%Y') for d in input_sorted], sep='\n')
