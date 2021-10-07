import math
import time

# Primes are sexy though, it goes without saying
# - Mr. Jackson

# Returns true if n is a prime number
def isPrime(n):
    if (n < 2): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    for factor in range(3,round(n**0.5)+1,2):
        if (n % factor == 0): return False
    return True
def almostEqual(a,b):
    return abs(a-b)<10**-10

# Returns two lists of X and Y values from a combined list of X and Y values
def splitToXY(L):
    xList = L[::2]
    yList = L[1::2]
    return xList, yList