target = 1000
max = 0
answer = 0

for i in range(1, target):
    if i % 2 == 0 or i % 5 == 0:
        continue

    n = 1
    while (10**n - 1) % i != 0:
        n += 1

    if max < n:
        max = n
        answer = i

print(answer)