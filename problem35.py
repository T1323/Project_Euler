from findPrimes import isPrime

def shiftNumber(input):
    str_num = str(input)
    length = len(str_num)
    return (int(str_num[1:length]) * 10 + int(str_num[0]))

def checkCircularPrime(input):
    number= shiftNumber(input)
    while number != input:
        if isPrime(number) == False:
            return False
        number = shiftNumber(number)
    return True

count = 13
even = {'2', '4', '6', '8', '0', '5'}
#l=[]
for i in range (101, 1000000):
    if set(str(i)) & even == set() and isPrime(i):
        if checkCircularPrime(i):
            count += 1
#            l.append(i)
#print(l)
print(count)

