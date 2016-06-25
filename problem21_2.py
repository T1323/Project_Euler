#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      phuang
#
# Created:     25/06/2016
# Copyright:   (c) phuang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from FindProperDivisors import findProperDivisorsSum

def main():
    dsum = [0 for i in range(40001)]
    amicableNums = list()

    for i in range(2, 10001):
        if dsum[i] == 0:
            dsum[i] = findProperDivisorsSum(i)

        b = dsum[i]
        if dsum[b] == i and b != i:
            if b not in amicableNums:
                amicableNums.append(i)
                amicableNums.append(b)
        elif dsum[b] == 0:
            dsum[b] = findProperDivisorsSum(b)

    answer = sum(amicableNums)
    print(answer)

if __name__ == '__main__':
    main()
