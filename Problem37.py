from findPrimes import isPrime

def checkTruncatePrime(input):
    input //= 10
    while (input):
        if isPrime(input) == False:
            return False
        input //= 10
    return True

answer = []
test = [3, 7]
count = 0
tryThis = [1, 2, 3, 5, 7, 9]
tens = 1

while (len(answer) < 11):
    numbers = test.copy()
    test = []
    tens *= 10
    for i in numbers:
        for j in tryThis:
            t = j * tens + i
            if isPrime(t):
                ret = checkTruncatePrime(t)
                if ret:
                    answer.append(t)
                    count = len(answer)
                test.append(t)

print(answer)
print(sum(answer))


