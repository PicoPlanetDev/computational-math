import math

def moveToBack(a,b):
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                a.remove(a[j])
                a.append(b[i])
    return a

print(moveToBack([2, 3, 3, 4, 1, 5], [3]))