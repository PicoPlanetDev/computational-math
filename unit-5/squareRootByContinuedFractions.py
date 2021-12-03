import math

def almostEqual(x,y):
    return abs(x-y)<10**-8

def continued_fraction(n):
    integer = int(n)
    decimal = n - integer
    cf_list = [integer]
    if decimal != 0:
        while integer != 2*cf_list[0]:
            decimal_inv = 1/decimal
            integer = int(decimal_inv)
            decimal = decimal_inv - integer
            cf_list.append(integer)
    return cf_list

def root(n, c):
    fraction_list = continued_fraction(math.sqrt(n))
    if len(fraction_list) == 1:
        return fraction_list[0]

    repeat = fraction_list[1:]
    i = 0
    while len(fraction_list) < c:
        fraction_list.append(repeat[i])
        i += 1
        if i == len(repeat):
            i = 0
    
    print(fraction_list)
    numerator = 0
    denominator = 1
    for i in range(c-1):
        numerator = 2 * denominator + numerator
        denominator = denominator + numerator
    return numerator, denominator

print(root(2,3))


# print(squareRootByContinuedFractions(2,2))
# print(squareRootByContinuedFractions(2,8))
# print(squareRootByContinuedFractions(2,50))