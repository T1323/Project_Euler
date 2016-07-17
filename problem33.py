from findPrimes import isPrime

prime100 = [2, 3, 5, 7, 11, 13, 17. 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def getL(a, b):
    re = 1
    for i in prime100:
        if i >= a:
            break
        else:
            while (a % i == 0 and b % i == 0):
                a /= i
                b /= i
                re *= i
    return [a, b]

cases = list()

for i in range(99, 10, -1):
    if isPrime(i):
        continue
    else:
        for j in range(i-1, 10, -1):
            if isPrime(j):
                continue
            else:
                set_a = set(str(j).split(''))
                set_b = set(str(i).split(''))
                set_c = set_a and set_b
                if len(set_c) == 1:
                    new_a = int(set_a ^ set_c)
                    new_b = int(set_b ^ set_c)

                old_value = getL(a, b)
                new_value = getL(new_a, new_b)
                if old_value == new_value:
                    cases.append([j, i])

