date = 1
count = 0
date += 366

big = (1, 3, 5, 7, 8, 10, 12)
small = (4, 6, 9, 11)

for y in range(1901, 2001):
    for m in range(1, 13):
        if m in big:
            date += 31
        elif m in small:
            date += 30
        elif ((m == 2 and y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
            date += 29
        else:
            date += 28

        date %= 7
        if date == 0:
            count += 1

if date == 0:
    count -= 1

print(count)
