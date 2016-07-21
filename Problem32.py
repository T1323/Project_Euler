def getDigitNumber(input):
    ret = []
    while input > 0:
        ret.append(input % 10)
        input //= 10
    return (set(ret))

answer = []
set0 = {0}
for i in range(9876, 122, -1):
    if i % 10 == 1:
        continue
    else:
        setA = getDigitNumber(i)
        if len(setA) == len(str(i)):
            for j in range(2, i):
                setB = getDigitNumber(j)
                if len(setA) + len(setB) > 5:
                    break
                elif j % 10 != 1 and len(setB) == len(str(j)):
                    p =i * j
                    setC = getDigitNumber(p)
                    if len(setC) == len(str(p)):
                        if len(setA) + len(setB) + len(setC) > 9:
                            break
                        if (len(setA | setB | setC | set0) == 10) and p not in answer:
                            answer.append(p)

print(sum(answer))

