f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def fractorialSum(input):
    ret = 0
    while input > 0:
        ret += f[input % 10]
        input //= 10
    return ret

print(sum([i for i in range(10, 2903040) if fractorialSum(i) == i]))
