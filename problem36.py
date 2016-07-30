def checkPalindromic(input):
    num_str = str(input)
    length = len(num_str)
    a = 0
    b = length - 1
    while (a < b):
        if num_str[a] != num_str[b]:
            return False
        a += 1
        b -= 1
    return True

def appendReverse(input, mode):
    number = input
    if mode == 1:
        input = (input << 1) | 0x0
    elif mode == 2:
        input = (input << 1) | 0x1

    while (number != 0):
        input = (input << 1) | (number % 2)
        number >>= 1
    return input

alist = [1]
for i in range(1, 700, 1):
    test = [appendReverse(i, j) for j in range(3)]
    for k in range(3):
        if checkPalindromic(test[k]) and test[k] < 1000000:
            alist.append(test[k])
print(sum(alist))