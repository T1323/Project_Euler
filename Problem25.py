count = 2
length = 0


f1 = 1
f2 = 1
while length < 1000:
    count += 1
    fn = f1 + f2
    f1 = f2
    f2 = fn
    length = len(str(fn))

print(count)
