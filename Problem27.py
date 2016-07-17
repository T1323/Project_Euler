from findPrimes import isPrime

oddNum = [i for i in range(1000) if i % 2 == 1]
answer = 1
maxNum = 0
negative = 0
aa = 0
bb = 0
for b in range(2, 1000):
    if isPrime(b) == False:
        continue
    else:
        for a in oddNum:
            count1 = 0
            count2 = 0
            n = 0
            negative = 0
            while isPrime(n**2 + a*n + b):
                count1 += 1
                n += 1

            n =0

            while isPrime(n**2 -a*n + b):
                count2 += 1
                n += 1

            if count2 > count1:
                count1 = count2
                negative ^= 1

            if count1 > maxNum:
                maxNum = count1
                answer = a*b*( (-1)**negative)
                aa = a
                bb = b
print(answer, aa, bb, maxNum)