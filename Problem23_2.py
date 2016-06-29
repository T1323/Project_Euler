from FindProperDivisors import findProperDivisorsSum as PSum

abundantList = list()
Oddabundant = list()

for i in range(12, 28123):
    if PSum(i) > i:
        abundantList.append(i)

for i in abundantList:
    if i % 2 == 1:
        Oddabundant.append(i)

answer = 0

for i in range(1, 47):
    isAdd = True
    if i % 2 == 0:
        index = 0
        while abundantList[index] <= (i // 2):
            if (i - abundantList[index]) in abundantList:
                isAdd = False
                break
            index += 1
    if isAdd:
        answer += i

for i in range(47, 28124, 2):
    isAdd = True
    index = 0
    while Oddabundant[index] < i:
        if (i - Oddabundant[index]) in abundantList:
            isAdd = False
            break
        index += 1
    if isAdd:
        answer += i

print(answer)
