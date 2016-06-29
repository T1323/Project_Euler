from FindProperDivisors import findProperDivisorsSum as PSum

Total = [i for i in range(1, 28124)]

abundantList = list()
Oddabundant = list()

for i in range(12, 28123):
    if PSum(i) > i:
        abundantList.append(i)

for i in abundantList:
    if (i + 12) in Total:
        Total.remove(i + 12)
    if i % 2 == 1:
        Oddabundant.append(i)

answer = 0

for j in Total:
    isAdd = True
    if j % 2 == 0:
        index = 1
        while abundantList[index] <= (j / 2):
            if (j - abundantList[index]) in abundantList:
                isAdd = False
                break
            index += 1
    else:
        index = 0
        while Oddabundant[index] < j:
            if (j - Oddabundant[index]) in abundantList:
                isAdd = False
                break
            index += 1
    if isAdd:
        answer += j

print(answer)
