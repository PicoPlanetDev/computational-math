import math

def almostEqual(x,y):
    return abs(x-y)<10**-8

def squareRootByContinuedFractions(r,c):
    i = 1
    while i**2 < r: i += 1
    p = i - 1
    x = 1
    for i in range(c): x = p + (r-p**2) / (p + x)
    return x

print("Instead of the numberator and denominator, this returns a decimal approximation")
print("Compare to math.sqrt(2): ", math.sqrt(2))
print(squareRootByContinuedFractions(2,1))
print(squareRootByContinuedFractions(2,2))
print(squareRootByContinuedFractions(2,8))
print(squareRootByContinuedFractions(2,50))