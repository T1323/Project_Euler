from FindProperDivisors import findProperDivisors

dsum = [0 for i in range(40001)]
amicableNums = list()

for i in range(2, 10001):
    if dsum[i] == 0:
        list_a = findProperDivisors(i)
        dsum[i] = sum(list_a)

    b = dsum[i]
    if dsum[b] == i and b != i:
        if b not in amicableNums:
            amicableNums.append(i)
            amicableNums.append(b)
    elif dsum[b] == 0:
        list_b = findProperDivisors(b)
        dsum[b] = sum(list_b)

answer = sum(amicableNums)
print(answer)