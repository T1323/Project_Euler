def numberStrToInt(str):
    str2 = str.split(' ')
    listint = [int(i) for i in str2]
    return listint

numbers = [[0 for i in range(15)] for j in range(15)]
row = [0 for i in range(15)]

row[0] = "75"
row[1] = "95 64"
row[2] = "17 47 82"
row[3] = "18 35 87 10"
row[4] = "20 04 82 47 65"
row[5] = "19 01 23 75 03 34"
row[6] = "88 02 77 73 07 63 67"
row[7] = "99 65 04 28 06 16 70 92"
row[8] = "41 41 26 56 83 40 80 70 33"
row[9] = "41 48 72 33 47 32 37 16 94 29"
row[10] = "53 71 44 65 25 43 91 52 97 51 14"
row[11] = "70 11 33 28 77 73 17 78 39 68 17 57"
row[12] = "91 71 52 38 17 14 91 43 58 50 27 29 48"
row[13] = "63 66 04 68 89 53 67 30 73 16 69 87 40 31"
row[14] = "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

for i in range(15):
    numbers[i] = numberStrToInt(row[i])

r = 14
while(r):
    for i in range(len(numbers[r-1])):
        numbers[r-1][i] += max(numbers[r][i], numbers[r][i+1])
    r -= 1

print(numbers[0][0])
