from calendar import monthcalendar as mc

y = int(input())
for i in range(1, 13):
    day = mc(y, i)[3][3] if mc(y, i)[0][3] == 0 else mc(y, i)[2][3]
    print(f"{day}.{str(i).zfill(2)}.{y}")
