from findPrimes import isPrime

prime100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def getL(a, b):
    re = 1
    for i in prime100:
        if i >= a:
            break
        else:
            while (a % i == 0 and b % i == 0):
                a //= i
                b //= i
                re *= i
    return [a, b]

def getI(a, b):
    set_a = set([a // 10, a % 10])
    set_b = set([b // 10, b % 10])
    set_c = set_a & set_b
    if len(set_c) != 1:
        return [0,0]
    list_new_a = list(set_a ^ set_c)
    list_new_b = list(set_b ^ set_c)
    new_a = int(list_new_a[0])
    new_b = int(list_new_b[0])

    return getL(new_a, new_b)



cases = list()

for a in range(99, 10, -1):
    if isPrime(a):
        continue
    else:
        digit = [a // 10, a % 10]
        if digit[1] == 0 or digit[0] == digit[1]:
            continue
        else:
            for i in digit:
                num_set_1 = (i * 10 + j for j in range(1,10) if i != j)
                for b in num_set_1:
                    if b >= a:
                        continue
                    elif getL(a, b) == getI(a, b):
                        cases.append([a, b])
                num_set_2 = (j * 10 + i for j in range(1, 10) if i != j)
                for b in num_set_2:
                    if b >= a:
                        continue
                    elif getL(a, b) == getI(a, b):
                        cases.append([a, b])
answer_a = 1
answer_b = 1
for l in cases:
    answer_a *= l[0]
    answer_b *= l[1]
r = getL(answer_a, answer_b)
print(r[0])
