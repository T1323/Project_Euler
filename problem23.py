from FindProperDivisors import findProperDivisorsSum as PSum

Total = [i for i in range(1, 28124)]

abundantList = list()

for i in range(1, 28123):
    if PSum(i) > i:
        abundantList.append(i)

length = len(abundantList)
for i in range(length - 1, -1, -1):
    for j in range(i+1):
        asum = abundantList[i] + abundantList[j]
        if asum > 28123:
            break
        elif asum in Total:
            Total.remove(asum)

print(sum(Total))
