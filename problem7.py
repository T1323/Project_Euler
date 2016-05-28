import math
primeList = [2]

for i in range(3, 1000000):
    isPrime = True
    stop = int(math.sqrt(i))
    for p in primeList:
        if p <= stop:
            if i % p == 0:
                isPrime = False
                break
        else:
            break
    if isPrime:
        primeList.append(i)
        if len(primeList) == 10001:
            #print(primeList)
            print(i)
            break