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

for i in Total:
    if i % 2 == 0:
        index = 1
        while abundantList[index] <= (i / 2):
            if (i - abundantList[index]) in abundantList:
                Total.remove(i)
                break
            index += 1
    else:
        index = 0
        while Oddabundant[index] < i:
            if(i - Oddabundant[index]) in abundantList:
                Total.remove(i)
                break
            index += 1

print(sum(Total))
