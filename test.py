import math

def sumOfProductsOfAllIntegerPairsLessThanN(n):
    total = 0
    for i in range(1,n):
        for j in range(1,n):
            total += i*j
    return total

print(sumOfProductsOfAllIntegerPairsLessThanN(4))