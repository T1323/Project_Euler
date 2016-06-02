import math

target = 600851475143

primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in range(101, 2000000):
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

ans = 0
for i in primeList:
    ans += i
print(ans)