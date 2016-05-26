import math

target = 600851475143

primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in range(101, 100000):
    isPrime = True
    stop = int(math.sqrt(i))
    for p in primeList:
        if p < stop:
            if i % p == 0:
                isPrime = False
                break
        else:
            break
    if isPrime:
        primeList.append(i)

#print(primeList)

stop = int(math.sqrt(target))
divider = []
found = False
for i in range(2, stop):
    if target % i == 0:
        divider.append(i)
        test = int(target / i)
        test_stop = int(math.sqrt(test))
        test_prime = True
        for x in primeList:
            if x < test_stop:
                if test % x == 0:
                    test_prime = False
                    break
            else:
                break
        if test_prime:
            found = True
            print(test)
            break
if found == False:
    for i in divider[::-1]:
        test = i
        test_stop = int(math.sqrt(test))
        test_prime = True
        for x in primeList:
            if x <= test_stop:
                if test % x == 0:
                    test_prime = False
                    break
            else:
                break
        if test_prime:
            found = True
            print(test)
            break
