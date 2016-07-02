import sys

fin = open(sys.argv[1], 'rt')
allText = fin.read()
allList = allText.split(',')
base = ord('A') - 1

group = [list() for i in range(26)]

for i in range(len(allList)):
    allList[i] = allList[i][1:len(allList[i]) - 1]
    iniChar = allList[i][0]
    group[ord(iniChar) - base - 1].append(allList[i])

count = 0
total = 0
for i in range(26):
    group[i].sort()
    for j in range(len(group[i])):
        count += 1
        sum = 0
        for k in range(len(group[i][j])):
            sum += ord(group[i][j][k]) - base
        total += (sum * count)

print(total)