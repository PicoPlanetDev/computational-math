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

def lookAndSay(L):
    if L==[]: return []
    said = []
    count = 1
    last = 0
    for i in range(len(L)-1):
        last = L[i]
        if L[i] == L[i+1]: 
            count += 1
        else:
            said.append((count,last))
            count = 1
    last = L[-1]
    said.append((count,last))
    return said

def makeLookAndSay(L,g):
    list = L
    for i in range(g):
        generation = []
        for j in range(len(lookAndSay(list))):
            generation.append(lookAndSay(list)[j][0])
            generation.append(lookAndSay(list)[j][1])
        list = generation
    return list

print(makeLookAndSay([3,3,7,7,7], 4))