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