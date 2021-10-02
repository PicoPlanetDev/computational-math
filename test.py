import math
import time

# Returns true if n is a prime number
def isPrime(n):
    if (n < 2): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    for factor in range(3,round(n**0.5)+1,2):
        if (n % factor == 0): return False
    return True

def degToRad(degrees):
    return degrees * (math.pi / 180)

def higherQuadraticFormula(a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return max(x1,x2)

def harderCannonAiming(initialHeight,targetRange):
    v0 = 600 #ft/s
    thetaStep = 0.01 #degrees
    g = 32 #ft/s^2
    bestDeviation = 0
    bestAngle = 0
    i = 0
    while i < 90:
        i = round(i+thetaStep, 2)
        theta = degToRad(i)
        v0y = v0 * math.sin(theta)
        v0x = v0 * math.cos(theta)
        tAir = higherQuadraticFormula(-0.5 * g, v0y, initialHeight)
        hit = v0x * tAir
        if i == 0.01:
            bestDeviation = abs(targetRange - hit)
            bestAngle = i
        else: 
            if abs(hit - targetRange) <= bestDeviation:
                bestDeviation = abs(hit - targetRange)
                bestAngle = i
            if abs(hit - targetRange) > bestDeviation:
                break
    return bestAngle

tests = [0.01, 0.01, 0.01, 4.78, 9.46, 13.86, 18.34, 23.24]

j = 0
for i in range(100,10**4,1257):
    print(harderCannonAiming(347,i))
    print(tests[j])
    print (tests[j] == harderCannonAiming(347,i))
    j += 1