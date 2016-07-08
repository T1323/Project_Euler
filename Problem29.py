from FindProperDivisors import findProperDivisors

target = 100
count = (target - 1) * (target - 1)

primeList = [2, 3, 5, 7, 11,13, 17]
removeList = list()

singleRound = [i for i in primeList if i * i <= target]

for i in singleRound:
    j = 1
    while i ** j <= target:
        for k in range(2, 101):
            tmp = j * k
            divisor = findProperDivisors(tmp)
            for l in divisor:
                if l > j and i ** l <= 100:
                    count -= 1
                    removeList.append(i ** (j * k))
                    break
        j += 1

twoRound = [i*j for i in primeList for j in primeList if (i*j) ** 2 <= 100 and i < j]

for i in twoRound:
    j = 1
    while i ** j <= target:
        for k in range(2, 101):
            tmp = j * k
            divisor = findProperDivisors(tmp)
            for l in divisor:
                if l > j and i ** l <= 100:
                    count -= 1
                    removeList.append(i ** (j * k))
                    break
        j += 1

print(count)