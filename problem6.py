target = 100

nums = range(1, target + 1)

sum1 = 0
for i in nums:
    sum1 += i

sum2 = 0
for i in range(1, target):
    sum1 -= i
    sum2 += i * sum1

print(2 * sum2)