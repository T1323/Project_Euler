gen = (i ** j for i in range(2, 101) for j in range(2, 101))

print(len(set(gen)))