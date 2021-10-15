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

# Returns two luckys of X and Y values from a combined lucky of X and Y values
def splitToXY(L):
    xlucky = L[::2]
    ylucky = L[1::2]
    return xlucky, ylucky

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
    lucky = L
    for i in range(g):
        generation = []
        for j in range(len(lookAndSay(lucky))):
            generation.append(lookAndSay(lucky)[j][0])
            generation.append(lookAndSay(lucky)[j][1])
        lucky = generation
    return lucky

# Returns the number of digits in n
def digitCount(n):
    n=abs(n)
    counter=0
    while True:
        n//=10
        counter+=1
        if (n==0): return counter

def isPrime(n):
    if (n < 2): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    for factor in range(3,round(n**0.5)+1,2):
        if (n % factor == 0): return False
    return True

def nthLuckyPrime(n):
    lucky=list(range(-1,n,2))
    i=2
    while lucky[i:]:
        lucky=sorted(set(lucky)-set(lucky[lucky[i]::lucky[i]]));i+=1
    del(lucky[0])
    for i in lucky:
        if not isPrime(i):
            del(lucky[lucky.index(i)])
    return lucky

# Returns the number of digits in n
def digitCount(n):
    n=abs(n)
    counter=0
    while True:
        n//=10
        counter+=1
        if (n==0): return counter

def carrylessAdd(x,y):
    result = 0
    place = 1
    result = 0
    while (x or y) :
        result = (((x % 10) + (y % 10))%10 * place) + result
        x = math.floor(x / 10)
        y = math.floor(y / 10)
        place *= 10
    return result

def carrylessMultiply(x,y):
    xLength = digitCount(x)
    yLength = digitCount(y)
    multSum = 0
    lineSum = 0
    for i in range(0,yLength):
        yDigit = (y//10**i)%10
        for j in range(0, xLength):
            xDigit = (x//10**j)%10
            multSum = multSum + (yDigit * xDigit)
        lineSum = carrylessAdd(lineSum, ((multSum)*10**i))
    return lineSum

print(carrylessMultiply(643,59))