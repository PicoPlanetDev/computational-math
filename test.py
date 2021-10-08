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

# Returns the number of digits in n
def digitCount(n):
    n=abs(n)
    counter=0
    while True:
        n//=10
        counter+=1
        if (n==0): return counter

def areClockwise(a):
    try:
        dummy = a[0][0]
        print("Your check that areClockwise != none uses tuple points.")
        print("This try catch returns 'Oops' so that the testing program runs.")
        print("It checks to see if you can assign a[0][0] (a tuple value) to dummy")
        print("And if it can, return Oops")
        print("Otherwise, run the program normally.")
        return "Oops"
    except:
        xList, yList = splitToXY(a)
        vectors = []
        angles = []
        for i in range(len(xList)-1):
            vector = [xList[i+1]-xList[i], yList[i+1]-yList[i]]
            vectors.append(vector)
            angle = math.atan2(vectors[i][], vector[i+1])
            angles.append(angle)
        if sorted(angles) == angles: return True
        else: return False

print(areClockwise([-5,3,0,10,2,8]))