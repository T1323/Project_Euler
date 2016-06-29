def rank(number):
    answer = 1
    for i in range(1, number + 1):
        answer *= i
    return answer

digits = [i for i in range(10)]
target = 1000000 - 1
r = 0
for i in range(9, 0, -1):
    divisor = rank(i)
    index = target // divisor
    target %= divisor
    d = digits[index]
    r += (10 ** i) * d
    digits.remove(d)


print(r)

