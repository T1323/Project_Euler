fifthPower = [i ** 5 for i in range(0, 10)]

answer = 0
for i in range(200, 300001):
    num_str = str(i)
    numList = [int(num_str[i]) for i in range(len(num_str))]
    sum = 0
    for j in numList:
        sum += fifthPower[j]
    if sum == i:
        answer += i

print(answer)