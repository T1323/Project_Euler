#-------------------------------------------------------------------------------
# Name:        Primes
# Purpose:
#
# Author:      phuang
#
# Created:     28/06/2016
# Copyright:   (c) phuang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def isPrime(number):
    if number <= 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        stop = int(number ** (0.5)) + 1
        i = 5
        while i < stop:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

def createPrimeTable(target):
    primeTable = list()
    for i in range(target + 1):
        if isPrime(i):
            primeTable.append(i)
    return primeTable

def main():
    print(createPrimeTable(100))

if __name__ == '__main__':
    main()
