element = [200, 100, 50, 20, 10,5, 2, 1]

def findComponent(target, component):
    count = 0
    length = len(component)
    if length == 1 or target == 0:
        return 1
    else:
        mainComponent = component[0]
        tmp = component[1:]
        while (target >= 0):
            r = findComponent(target, tmp)
            count += r
            target -= mainComponent
        return count

answer = findComponent(200, element)
print(answer)
