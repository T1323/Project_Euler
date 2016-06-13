import math

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#def buildPrime(target, prime):
#    for i in range(101, target):
#        isPrime = True
##        stop = int(math.sqrt(i))
 #       for p in prime:
 #           if p < stop:
 ##               if i % p == 0:
 #                   isPrime = False
 #                   break
 #           else:
 #               break
 #       if isPrime:
 #           prime.append(i)

def findFactor( number, x):
    index = 0
    for p in prime:
        count = 0
        while number % p == 0:
            count += 1
            number //= p
        x[index] = count
        index += 1
        if number == 1:
            break

answer = 1
#buildPrime(20000, prime)
while True:
    x0 = [0 for i in range(len(prime))]
    x1 = [0 for i in range(len(prime))]
    findFactor(answer, x0)
    findFactor(answer + 1, x1)
    x2 = [i + j for i, j in zip(x0, x1)]
    x2[0] -= 1
    factors = 1
    for x in x2:
        factors *= (x + 1)
    if factors > 500:
        break
    else:
        answer += 1

print(answer * (answer+ 1) // 2)