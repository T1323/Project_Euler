PrimeNumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def findProperDivisors(number):
    divisorPair = dict()
    stop = int(number ** (0.5))

    for i in range(1, stop + 1):
        if number % i == 0:
            divisorPair[i] = number // i

    list_1 = list(divisorPair.keys())
    list_2 = list(divisorPair.values())
    if stop in list_2:
        list_2.remove(stop)
    list_3 = list_1 + list_2[::-1]
    list_3.remove(number)
    return list_3

def findProperDivisorsSum(number):
    inputValue = number
    stop = int(number**(0.5)) + 1
    divisor = 2
    PDSum = 1
    while divisor < stop and number > 1:
        if number % divisor == 0:
            tmp = divisor * divisor
            number //= divisor
            while number % divisor == 0:
                tmp *= divisor
                number //= divisor

            PDSum *= (tmp - 1) // (divisor - 1)
        if divisor == 2:
            divisor = 3
        else:
            divisor += 2
    if number != 1:
        PDSum *= (number + 1)
    PDSum -= inputValue
    return PDSum



