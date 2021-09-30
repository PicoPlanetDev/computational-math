##############################################################################
##    Unit Two Starting Point
##    DO NOT CHANGE THE NAMES OF THE PROGRAMS!!!!!
##    Replace None with your code.
##    If you don't submit one of these programs, leave None in place.
##    almostEqual is provided
##############################################################################

import math

# Returns true if the difference between x and y is less than 10^-10
def almostEqual(x,y):
    return abs(x-y)<10**-10

# Returns true if n is a prime number
def isPrime(n):
    if (n < 2): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    for factor in range(3,round(n**0.5)+1,2):
        if (n % factor == 0): return False
    return True

# Returns the number of digits in n
def digitCount(n):
    n=abs(n)
    counter=0
    while True:
        n//=10
        counter+=1
        if (n==0): return counter

# Returns the kth digit of n counting from the right  
def kthDigit(n, k):
    return int(abs(n) // (10**k) % 10)

# Returns true if n has at least two digits next to each other that are the same
def hasConsecutiveDigits(n):
    if digitCount(n) <= 1: return False
    for i in range(digitCount(n)):
        if kthDigit(n, i) == kthDigit(n, i+1):
            return True
    return False

# Replaces the kth digit k of a number n with the digit d returning the result
def setKthDigit(n, k, d):
    return n-((n//10**k)%10*10**k)+(10**k*d)

# Helper function for isPandigital
# Returns true if n includes the digit d somewhere
def doesInclude(n, d):
    for i in range(digitCount(n)):
        if kthDigit(n, i) == d: return True
    return False

# Determines if a number n is pandigital by checking if it includes each number in range 0-9
def isPandigital(n):
    for i in range(10):
        if not doesInclude(n, i): return False
    return True

# Helper function for mostFrequentDigit
# Counts how many times a digit d occurs in n
def countOccurrences(n, d):
    count = 0
    while n:
        if (n % 10 == d): count += 1
        n = int(n / 10)
    return count

# Finds the most frequent digit in a number n
def mostFrequentDigit(n):
    n = abs(n)
    result = 0
    maxCount = 1
    for d in range(10): 
        count = countOccurrences(n, d)
        if (count >= maxCount):
            maxCount = count
            result = d
    return result

# Mr. Jackson says: 
# I lived in fear of Soham. Everything I said, I feared he was going to correct me.

# Ask about this one! When I try
# for x in range(1, math.ceil(n**0.5)+1):
# The program hangs and my fans rev up
# Helper function for nthPerfectNumber
def isPerfectNumber(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

# Returns the nth perfect number
# Beware: this function is slow for large values of n (e.g. n>3)
def nthPerfectNumber(n):
    current = 6
    perfectCount = -1
    while perfectCount <= n:
        if isPerfectNumber(current): perfectCount += 1
        if perfectCount == n: return current
        current += 1

# Returns the greatest common divisor of a and b
def gcd(a,b):
    return math.gcd(a,b)

# Computes cosine(x) using a Taylor series then reutrns the difference between the computed value and cos(x)
def cosineError(x,k):
    #return abs(math.cos(x) - (10**k) * (sum([math.factorial(9*i)*kthDigit(x,9*i) for i in range(k)])))
    return None

# Helper function for isRotation
def findRotations(n, rotations):
    number = n
    digit = digitCount(number)
    power = pow(10, digit - 1)
    for i in range(rotations - 1):
        firstDigit = number // power
        left = (number * 10 + firstDigit - (firstDigit * power * 10))
        number = left
    return number

# Returns true if x is a rotation of y or y is a rotation of x, otherwise returns false
def isRotation(x,y):
    if (x==y): return True
    for i in range(digitCount(x)+1):            
        if findRotations(x,i)==y: return True
    for i in range(digitCount(y)+1):            
        if findRotations(y,i)==x: return True
    return False

# def longestDigitRun(n):
    # maxRun = 0
    # currentRun = 0
    # lastDigit = 0
    # lowestRunDigit = 9
    # for i in range(0,digitCount(n)):
    #     digit = kthDigit(n,i)
    #     if digit==lastDigit: currentRun+=1
    #     else: currentRun = 0
    #     if currentRun>=maxRun:
    #         #print("Currentrun, Maxrun: " + str(currentRun), str(maxRun))
    #         maxRun = currentRun
    #         if digit<=lowestRunDigit:
    #             lowestRunDigit = digit
    #             #print("Set lowest run digit to: " + str(lowestRunDigit))
    #     lastDigit = digit
    # return lowestRunDigit

# Mr. Jackson, this longest digit run is a mess, but I guarantee that if the commented out version above actually worked, I would have used it.
# If you can spot a way to make it work, please let me know. I pretty much had to give up on it after a week.
def longestDigitRun(n):
    n = abs(n)
    run0, run1, run2, run3, run4, run5, run6, run7, run8, run9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    lastDigit = -1
    lowestDigit = 9
    for i in range(0,digitCount(n)):
        digit = kthDigit(n,i)
        if digit < lowestDigit: lowestDigit = digit
        if digit==lastDigit:
            if digit==0: run0+=1
            elif digit==1: run1+=1
            elif digit==2: run2+=1
            elif digit==3: run3+=1
            elif digit==4: run4+=1
            elif digit==5: run5+=1
            elif digit==6: run6+=1
            elif digit==7: run7+=1
            elif digit==8: run8+=1
            elif digit==9: run9+=1
        lastDigit = digit
    maxRunLength = max(run0, run1, run2, run3, run4, run5, run6, run7, run8, run9)
    if maxRunLength==0: return lowestDigit
    elif run0 == maxRunLength: return 0
    elif run1 == maxRunLength: return 1
    elif run2 == maxRunLength: return 2
    elif run3 == maxRunLength: return 3
    elif run4 == maxRunLength: return 4
    elif run5 == maxRunLength: return 5
    elif run6 == maxRunLength: return 6
    elif run7 == maxRunLength: return 7
    elif run8 == maxRunLength: return 8
    elif run9 == maxRunLength: return 9

def longestIncreasingRun(n):
    return None

def reverseNumber(n):
    num = n
    reverse = 0
    while(num>0):
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num//10
    return reverse

def isPalindromic(n):
    return n == reverseNumber(n)

def isPalindromicPrime(n):
    if isPalindromic(n) and isPrime(n): return True

def nthPalindromicPrime(n):
    found = -1
    count = 0
    while found <= n:
        if isPalindromicPrime(count):
            found += 1
        if found == n: return count
        count += 1

def nthLeftTruncatablePrime(n):
    return None

# def isPowerful(n):
#     while (n % 2 == 0):
#         power = 0
#         while (n % 2 == 0):
#             n = n//2
#             power = power + 1
#         if (power == 1):
#             return False
#     for factor in range(3, int(math.sqrt(n))+1, 2):
#         power = 0
#         while (n % factor == 0):      
#             n = n//factor
#             power = power + 1
#         if (power == 1):
#             return False
#     return (n == 1)

# def nthPowerfulNumber(n):
#     found = -1
#     count = 0
#     while found <= n:
#         if isPowerful(count):
#             found += 1
#         if found == n: return count
#         count += 1

def nthPowerfulNumber(n):
    return None

def isStrobogrammaticNumber(n):
    return None

# Helper function for isHappyNumber
def sumOfSquaresOfDigits(n):
    total=0
    if (n==0):return 0
    while (n!=0):
        total+=(n%10)**2
        n//=10
    return total

# Helper function for nthHappyNumber and nthHappyPrime
def isHappyNumber(n):
    if (n<=0):return False
    if (n==1):return True
    total=sumOfSquaresOfDigits(n)
    while (total!=4):
        total=sumOfSquaresOfDigits(total)
        if (total==1):return True
    return False

def nthHappyNumber(n):
    x=0
    counter=-1
    while True:
        if (isHappyNumber(x)): counter+=1
        if (counter==n):return x
        x+=1

def nthHappyPrime(n):
    counter=-1
    x=2
    while True:
        if(isHappyNumber(x) and isPrime(x)): counter+=1
        if (counter==n):return x
        x+=1

# Helper function for nearestKaprekarNumber
def isKaprekarNumber(n):
    if (n==0): return False
    if (n==1): return True
    nsquare=n**2
    digitOfRightNum=0
    while True:
        digitOfRightNum+=1
        if(nsquare%10**digitOfRightNum==0):continue
        if(nsquare//10**digitOfRightNum==0):return False
        b=nsquare%10**digitOfRightNum
        a=nsquare//10**digitOfRightNum
        if(a+b==n):return True

# Finds the nearest Kaprekar number to n
def nearestKaprekarNumber(n):
    #print("Finding nearest kaprekar of " + str(n) + "... This may take a while.")
    delta=-1
    while True:
        delta+=1
        np = math.ceil(n+delta)
        nm = math.floor(n-delta)
        if(isKaprekarNumber(np)):
            if isKaprekarNumber(nm):
                if abs(nm-n)<=abs(np-n): return nm
                return np
            return np
        if(isKaprekarNumber(nm)):
            if isKaprekarNumber(np):
                if abs(nm-n)<=abs(np-n): return nm
                return np
            return nm

def nthCarolPrime(n):
    x=2
    counter=-1
    while True:
        if (isPrime((2**x-1)**2-2)): counter+=1
        if (counter==n):return ((2**x-1)**2-2)
        x+=1

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

def integral(f, a, b, N):
    interval=(b-a)/N
    s=0
    for n in range(0,N+1):
        s+=f(a+n*interval)
    return (interval*(2*s-f(a)-f(b))/2)

def findZeroWithBisection(f,x0,x1,epsilon):
    runs = 0
    maxruns = 1000
    while runs<maxruns:
        x=(x0+x1)/2
        if f(x)==0: return x
        if abs(x0-x1)<epsilon: return abs(x0-x1)/2 + x0 # Still not right
        signfx=math.copysign(1,f(x))
        signfx0=math.copysign(1,f(x0))
        if signfx == signfx0: x0=x
        else: x1=x
        runs+=1
    return "No zero in that range"


#############################################################################
##  GRADING TEST CASES
#############################################################################

x=[-8184082526, 4152289136, -150658491, 8363844277, -7691698362,
   -8194890099, -9697298147, -9389785424, -6710604572, -1244730739,
   -2026648117, 2211624042, -7345181586, -5000752345, 7221626837,
   1068703985, 2823219242, 3529494556, 3165807616, 4306182994, 9467091544,
   726094686, -1747047084, 9033614095, -3455443311, -5626826779, -80060854,
   4097366650, 4439904879, -4316006873, 7767610460, 1156516251, 9910710188,
   5747065142, -9074730550, 2171446224, 2833796769, -793805149, 8501952802,
   -4322434004, -6268889918, -6800942908, -1732779408, -2348796962,
   -9918612277, 567114010, -7515795250, -6010068403, 3941367899,
   -6661484995, -1074962279, 1680694824, -4972630280, -3239484295,
   -3838195390, 4898235066, 4235972196, 5821739235, -6480120029,
   -1574824225, 3023978554, 5553133399, -3009865771, 5994614100,
   2737019587, -2067106692, -5014912191, 7905867271, 1543850190,
   -9313079225, 5770421382, 799239240, -3543311198, -1470972061,
   7340668206, 4488759562, 728810521, -9294211775, 8849853685, -7231899670,
   -854493981, -3885190640, -4161061572, 6217449678, -5247903312, 163613216,
   9951497564, -8534371981, 7482058869, -2141132294, -7042398694,
   9540422789, -7316957039, -2710339255, 690764464, 2808120345, -5596666139,
   -6177141609, 7611861265, -8984557519]

z=[-429571155745307, -410396842066983, -804248252055278, 877994461662702,
   687227856095050, 177656420982093, 280682179114644, 977765874900856,
   375441803320118, 78768131851725, 208440750364838, -846452512882854,
   -634629478930846, 545324279109823, 63033671986952, 700212945711221,
   -754546433144975, 336149455073568, -511126542545574, -963846069016693,
   -373717541263591, -255058709122438, 134990586817414, 299929342646711,
   632983221195854]

def getPrimes(n):
    primes=[False,False,True]+[False]*(n-3)
    sieve=[True]*n
    for p in range(3,n,2):
        if sieve[p]:
           primes[p]=True
           for i in range(p**2,n+1,2*p):
               sieve[i]=False
    return primes

def testIsPrime():
    global total
    assert isPrime(10000139)
    assert not isPrime(100000)
    assert not isPrime(2**3*3**5*5)
    assert not isPrime(1)
    assert not isPrime(25)
    assert [isPrime(i) for i in range(2,10**5)]==getPrimes(10**5)[2:]
    print('isPrime...Passed...5pts')
    total+=5
    
def testDigitCount():
    global total
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    assert digitCount(-1234567890987654321234567890987687687687665412461236587) \
           ==len(str(1234567890987654321234567890987687687687665412461236587))
    assert [digitCount(item) for item in x]== \
    [10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
     10, 10, 9, 10, 10, 10, 10, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9,
     10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
     10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10, 10,
     9, 10, 10, 10, 9, 10, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 9,
     10, 10, 10, 10, 10]
    assert [digitCount(10**i) for i in range(10)]== \
           [round(math.log(10**i,10))+1 for i in range(10)]
    print('digitCount...Passed...5 pts')
    total+=5

def testHasConsecutiveDigits():
    global total
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    assert hasConsecutiveDigits(-33) == True
    assert hasConsecutiveDigits(-31) == False
    assert hasConsecutiveDigits(-1234567898765432133) == True
    assert hasConsecutiveDigits(-1) == False
    assert [hasConsecutiveDigits(item) for item in x]== \
    [False, True, False, True, False, True, False, False, False, True, True,
     True, False, True, True, False, False, True, False, True, True, False,
     False, True, True, True, True, True, True, True, True, True, True, False,
     True, True, True, False, False, True, True, True, True, False, True, True,
     False, True, True, True, True, False, False, False, False, True, False,
     False, True, True, True, True, True, True, False, True, False, False,
     False, True, True, True, True, False, True, True, True, True, True, True,
     True, True, False, True, True, False, True, False, True, True, False,
     True, False, True, True, False, True, True, True, True]
    print('hasConsecutiveDigits...Passed...8 pts')
    total+=8

def testIsPandigital():
    global total
    assert isPandigital(0)==False
    assert isPandigital(123456789)==False
    assert isPandigital(1234567890)==True
    assert isPandigital(1234444444444567890)==True
    assert isPandigital(112344444456789)==False
    pandos=[1023456789,1023456798,1023456879,1023456897,
     1023456978,1023456987,1023457689,1023457698,
     1023457869,1023457896,1023457968,1023457986,
     1023458679,1023458697,1023458769,1023458796,
     1023458967,1023458976,1023459678,1023459687,
     1023459768]
    for pando in pandos:assert isPandigital(pando)
    assert [isPandigital(abs(item)) for item in z]== \
    [False, False, False, False, False, True, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False,
     False, False, False]           
    print('isPandigital...Passed...8 pts')
    total+=8

def testMostFrequentDigit():
    global total
    assert mostFrequentDigit(0)==0
    assert mostFrequentDigit(1223)==2
    assert mostFrequentDigit(12233)==3
    assert mostFrequentDigit(-12233)==3
    assert mostFrequentDigit(1223322332)==2
    assert mostFrequentDigit(123456789)==9
    assert mostFrequentDigit(1234567789)==7
    assert mostFrequentDigit(1000123456789)==0
    assert mostFrequentDigit(102345678990011)==1
    assert [mostFrequentDigit(item) for item in x]== \
    [8, 2, 5, 8, 6, 9, 9, 9, 7, 7, 6, 2, 8, 5, 2, 8, 2, 5, 6, 9, 4, 6, 7, 9, 4,
     6, 0, 6, 9, 6, 7, 1, 1, 7, 0, 4, 9, 9, 8, 4, 8, 0, 7, 9, 9, 1, 5, 0, 9, 6,
     9, 8, 2, 9, 3, 8, 9, 5, 0, 2, 5, 3, 7, 9, 7, 6, 1, 7, 5, 9, 7, 9, 3, 7, 6,
     8, 8, 9, 8, 9, 9, 8, 1, 7, 3, 6, 9, 8, 8, 2, 9, 9, 9, 5, 6, 8, 6, 1, 6, 5]
    print('mostFrequentDigit...Passed...10 pts')
    total+=10

def testNthPerfectNumber():
    global total
    assert(nthPerfectNumber(0) == 6)
    assert(nthPerfectNumber(1) == 28)
    assert(nthPerfectNumber(2) == 496)
    import time
    start=time.time()
    assert(nthPerfectNumber(3) == 8128)
    print('nthPerfectNumber...Passed...10 pts')
    total+=10
    if time.time()-start<.05:
        total+=5
        print('5 Point time bonus for perfect number search')

def testGcd():
    global total
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5)==15)
    a = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(a, y) == g)
    assert [gcd(abs(x[i]),abs(x[i+1])) for i in range(len(x)-1)]== \
        [2, 1, 1, 1, 3, 1, 1, 4, 7, 1, 173, 6, 1, 1, 1, 1, 2, 4, 2, 2, 2, 6,
         1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 3, 1, 1, 14, 2, 2, 4, 298, 1,
         1, 10, 1, 1, 1, 1, 1, 8, 5, 5, 2, 6, 3, 1, 1, 1, 1, 11, 1, 1, 1, 3,
         1, 1, 5, 1, 6, 2, 1, 1, 74, 1, 1, 5, 5, 1, 1, 4, 6, 18, 16, 4, 1, 1,
         1, 2, 1, 1, 1, 13, 1, 1, 1, 1, 1]
    print('gcd...Passed...5 pts')
    total+=5

def testCosineError():
    global total
    assert(almostEqual(cosineError(0, 0), abs(math.cos(0) - 1)))
    assert(almostEqual(cosineError(1, 0), abs(math.cos(1) - 1)))
    x = 1.2
    guess = 1 - x**2/2 + x**4/(4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 2), error))
    x = 0.75
    guess = 1 - x**2/2 + x**4/(4*3*2) - x**6/(6*5*4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 3), error))
    for i in range(-40,50):
        x=i/10
        guess = 1 - x**2/2 + x**4/(4*3*2) - x**6/(6*5*4*3*2)+x**8/math.factorial(8)
        error = abs(math.cos(x) - guess)
        assert(almostEqual(cosineError(x, 4), error))
    
    print('cosineError...Passed 10 pts')
    total+=10

def testIsRotation():
    global total
    assert isRotation(2,2)==True
    assert isRotation(23456,23456)==True
    assert isRotation(3412,1234)==True
    assert isRotation(321,3210)==True
    assert isRotation(23,34)==False
    assert isRotation(123456789,567891234)==True
    assert isRotation(123400000,1234)==True
    assert isRotation(1234,1234*10**100)==True
    assert isRotation(3412,12034)==True
    assert isRotation(3412,12*10**100+34)==True
    assert isRotation(2468,24678)==False
    assert isRotation(1234,1423)==False
    import random
    a,rots=random.randrange(10**30,10**31)*10**10,[]
    length=len(str(a))
    for i in range(length):
        a=a//10+a%10*10**(length-1)
        rots.append(a)
    for rot in rots:assert isRotation(a,rot)
    b=[random.randint(10**30,10**31) for i in range(1000)]
    c=[item for item in b if sum([int(digit) for digit in sorted(str(item))])==134]
    for item in c: assert not isRotation(9302574275054101585464842598821,item)
    print('isRotation...Passed...10 pts')
    total+=10

def testLongestDigitRun():
    global total
    assert longestDigitRun(2)==2
    assert longestDigitRun(23)==2
    assert longestDigitRun(2341)==1
    assert longestDigitRun(-8)==8
    assert longestDigitRun(223344556677)==2
    assert longestDigitRun(2233445556677)==5
    assert longestDigitRun(-223344556677)==2
    assert longestDigitRun(22333445566777)==3
    assert longestDigitRun(223344556677)==2
    assert longestDigitRun(22334455667711)==1
    assert longestDigitRun(-123454321001234567899876543)==0
    assert longestDigitRun(-123454321012345678987654321)==0
    assert longestDigitRun(1122299933388832)==2
    assert [longestDigitRun(item) for item in x]== \
    [0, 2, 0, 4, 1, 0, 1, 2, 0, 4, 1, 1, 1, 0, 2, 0, 1, 5, 0, 9, 4, 0, 0, 3, 1, 7,
    0, 6, 4, 0, 7, 1, 8, 0, 5, 2, 3, 0, 0, 0, 8, 0, 7, 2, 2, 1, 0, 0, 9, 6, 2, 0,
    0, 2, 0, 6, 1, 1, 0, 2, 5, 3, 0, 0, 0, 6, 0, 0, 0, 2, 7, 9, 1, 0, 6, 4, 8, 1,
    8, 9, 4, 8, 0, 4, 3, 1, 9, 1, 8, 1, 0, 2, 0, 3, 4, 0, 6, 7, 1, 5]
    print('longestDigitRun...Passed...15 pts')
    total+=15

def testLongestIncreasingRun():
    global total
    assert longestIncreasingRun(2341)==234
    assert longestIncreasingRun(2345)==2345
    assert longestIncreasingRun(54321)==5
    assert longestIncreasingRun(123345)==345
    assert longestIncreasingRun(12345)==12345
    assert longestIncreasingRun(112233445566778899)==89
    assert longestIncreasingRun(1234234534564567567)==4567
    assert longestIncreasingRun(1234365283789394)==3789
    assert longestIncreasingRun(9876543210)==9
    assert [longestIncreasingRun(abs(item)) for item in x]== \
    [26, 289, 58, 38, 169, 489, 147, 389, 457, 124, 48, 24, 345, 2345, 268, 68,
     28, 56, 58, 29, 467, 468, 47, 36, 345, 268, 8, 36, 79, 68, 67, 156, 18,
     57, 47, 46, 379, 149, 28, 34, 268, 68, 79, 2348, 27, 567, 1579, 68,
     136789, 148, 279, 168, 49, 239, 39, 489, 2359, 235, 48, 157, 239, 39, 57,
     59, 58, 69, 149, 79, 38, 79, 138, 239, 35, 147, 68, 59, 28, 29, 368, 189,
     49, 38, 157, 678, 2479, 36, 149, 37, 69, 29, 239, 2789, 169, 39, 69, 345,
     139, 17, 126, 89]
    print('longestIncreasingRun...Passed...15 pts')
    total+=15


def testNthPalindromicPrime():
    import time
    global total
    assert nthPalindromicPrime(0)==2
    assert nthPalindromicPrime(4)==11
    assert nthPalindromicPrime(10)==313
    start=time.time()
    assert [nthPalindromicPrime(i) for i in range(30)]==\
           [2, 3, 5, 7, 11, 101, 131, 151, 181, 
            191, 313, 353, 373, 383, 727, 757, 787, 
            797, 919, 929, 10301, 10501, 10601, 11311, 
            11411, 12421, 12721, 12821, 13331, 13831]
    end=time.time()
    assert (end-start<1)
    print('nthPalindromicPrime...Passed...10 pts')
    total+=10

def testNthLeftTruncatablePrime():
    global total
    assert nthLeftTruncatablePrime(0)==2
    assert nthLeftTruncatablePrime(1)==3
    assert nthLeftTruncatablePrime(4)==13
    assert nthLeftTruncatablePrime(10)==53
    assert [nthLeftTruncatablePrime(i) for i in range(100)]== \
           [2, 3, 5, 7,13,17, 23, 37, 43, 47, 53, 67, 73, 83, 97, 
            113, 137, 167, 173, 197, 223, 283, 313, 317, 337, 347, 353, 367, 373, 
            383, 397, 443, 467, 523, 547, 613, 617, 643, 647, 653, 673, 683, 743, 
            773, 797, 823, 853, 883, 937, 947, 953, 967, 983, 997, 
            1223, 1283, 1367, 1373, 1523, 1613, 1823, 1997, 2113, 2137, 2347, 2383, 
            2467, 2617, 2647, 2683, 2797, 2953, 3137, 3167, 3313, 3347, 3373, 3467, 
            3547, 3613, 3617, 3643, 3673, 3797, 3823, 3853, 3947, 3967, 4283, 4337, 
            4373, 4397, 4523, 4547, 4643, 4673, 4937, 4967, 5113, 5167]
    print('nthLeftTruncatablePrime...Passed...8 pts')
    total+=8

def testNthPowerfulNumber():
    global total
    assert nthPowerfulNumber(0)==1
    assert nthPowerfulNumber(10)==64
    assert [nthPowerfulNumber(i) for i in range(54)]== \
           [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81, 100, 108, 121, 125, 128, 
            144, 169, 196, 200, 216, 225, 243, 256, 288, 289, 324, 343, 361, 392, 400, 
            432, 441, 484, 500, 512, 529, 576, 625, 648, 675, 676, 729, 784, 800, 841, 
            864, 900, 961, 968, 972, 1000]
    print('nthPowerfulNumber...Passed...8 pts')
    total+=8
    

def testIsStrobogrammaticNumber():
    global total
    assert isStrobogrammaticNumber(2)==False
    assert isStrobogrammaticNumber(6)==False
    assert isStrobogrammaticNumber(686)==False
    assert isStrobogrammaticNumber(868)==False
    assert isStrobogrammaticNumber(6886)==False
    assert isStrobogrammaticNumber(68389)==False
    assert [i for i in range(10**5) if isStrobogrammaticNumber(i)]== \
            [0, 1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689,
            808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 
            6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 
            9696, 9886, 9966, 10001, 10101, 10801, 11011, 11111, 11811, 16091, 
            16191, 16891, 18081, 18181, 18881, 19061, 19161, 19861, 60009, 
            60109, 60809, 61019, 61119, 61819, 66099, 66199, 66899, 68089, 
            68189, 68889, 69069, 69169, 69869, 80008, 80108, 80808, 81018, 
            81118, 81818, 86098, 86198, 86898, 88088, 88188, 88888, 89068, 
            89168, 89868, 90006, 90106, 90806, 91016, 91116, 91816, 96096, 
            96196, 96896, 98086, 98186, 98886, 99066, 99166, 99866]
    print('isStrobogrammaticNumber...Passed...10 pts')
    total+=10
happies=[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100,
         103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226,
         230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329,
         331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409,
         440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622,
         623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694]

def testNthHappyNumber():
    global total
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    assert [nthHappyNumber(i) for i in range(len(happies))]==happies
    print('nthHappyNumber...Passed...8pts')
    total+=8

def testNthHappyPrime():
    global total
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(10) == 167)
    assert(nthHappyPrime(20) == 397)
    assert [item for item in happies if isHappyNumber(item) and isPrime(item)]== \
           [7, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263, 293, 313, 331,
            367, 379, 383, 397, 409, 487, 563, 617, 653, 673, 683]
    print('nthHappyPrime...Passed...8 pts')
    total+=8

def testNearestKaprekarNumber():
    global total
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    assert [nearestKaprekarNumber(i**2+5*i+6) for i in range(1,10**3,157)]== \
        [9, 22222, 99999, 208495, 390313, 627615, 857143]
    print('nearestKaprekarNumber...Passed...10 pts')
    total+=10

def testNthCarolPrime():
    global total
    import time
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(2) == 223)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(6) == 16769023)
    assert(nthCarolPrime(8) == 68718952447)
    start=time.time()
    assert(nthCarolPrime(9) == 274876858367)
    end=time.time()
    if end-start<.3:
        print('nthCarolPrime...Passed...10 pts')
        total+=10
    else:
        print('nthCarolPrime...Passed...But too Slow...5 pts')
        total+=5

def testCarrylessAdd():
    global total
    assert carrylessAdd(785, 376)==51
    assert carrylessAdd(670785, 376)==670051
    assert carrylessAdd(670785, 89376)==659051
    assert [carrylessAdd(i,i) for i in range(77)]== \
            [0,2,4,6,8,0,2,4,6,8,20,22,24,26,28,20,22,24,26,
            28,40,42,44,46,48,40,42,44,46,48,60,62,64,66,68,
            60,62,64,66,68,80,82,84,86,88,80,82,84,86,88,0,2,
            4,6,8,0,2,4,6,8,20,22,24,26,28,20,22,24,26,28,40,
            42,44,46,48,40,42]
    print('carrylessAdd...Passed...10 points')
    total+=10



def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def f5(x): return x**2+5*x+6
def i5(x): return x**3/3+5*x**2/2+6*x

def testIntegral():
    def almostEqual(a,b):
        return abs(a-b)<10**-4
    global total
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5))))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5))))
    assert(almostEqual(integral(f2, 1, 2, 1), 4))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1))))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4))))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1))))
    assert(almostEqual(integral(f5, -5, 3, 1000), (i5(3)-i5(-5))))
    print('integral...Passed...10 pts')
    total+=10


def f6(x): return x**5-2**x
def f7(x): return math.sin(x)
def f8(x): return x**2-2

def testFindZeroWithBisection():
    global total
    assert findZeroWithBisection(f8, 1, 2, 0.1)==1.40625
    assert findZeroWithBisection(f1,-1,0,10**-10)=='No zero in that range'
    assert findZeroWithBisection(f2,-1,0,10**-10)==-0.5
    assert findZeroWithBisection(f4,math.pi*10,math.pi*11,10**-10)== \
           32.98672286264711
    assert findZeroWithBisection(f5,-3.1,-2.9,10**-10)==-3.0
    assert findZeroWithBisection(f5,-math.pi,-2.9,10**-1)==-2.9905972450961724
    assert findZeroWithBisection(f6,0,2,10**-1)==1.15625
    assert findZeroWithBisection(f6,0,2,10**-13)==1.1772785503550551
    assert findZeroWithBisection(f7,-math.pi*100-.01,-math.pi*100+.1,10**-13)== \
           -314.15926535897927
    def f(x):return math.cos(x)
    assert [round(findZeroWithBisection(f,1.4*i,1.4*i+0.8,10**-10),2) for i in range(100)
            if type(findZeroWithBisection(f,1.4*i,1.4*i+0.8,10**-10))!=str]== \
        [1.57, 4.71, 14.14, 17.28, 26.7, 29.85, 32.99, 39.27, 42.41, 45.55,
         51.84, 54.98, 58.12, 64.4, 67.54, 70.69, 80.11, 83.25, 92.68, 95.82,
         105.24, 108.38, 117.81, 120.95, 130.38, 133.52]
    print('findZeroWithBisection...Passed...10 pts')
    total+=10



#############################################################################
#############################################################################

def testAll():
    if isPrime(1)!=None:
        testIsPrime()
        pass               
    if digitCount(1)!=None:
        testDigitCount()
        pass
    if hasConsecutiveDigits(1)!=None:
        testHasConsecutiveDigits()
        pass
    if mostFrequentDigit(1)!=None:
        testMostFrequentDigit()
        pass
    if isPandigital(1)!=None:
        testIsPandigital()
        pass
    if nthPerfectNumber(0)!=None:
        testNthPerfectNumber()
        pass
    if gcd(1,1)!=None:
        testGcd()
        pass
    if cosineError(1,1)!=None:
        testCosineError()
        pass
    if isRotation(1,1)!=None:
        testIsRotation()
        pass
    if longestDigitRun(1)!=None:
        testLongestDigitRun()
        pass
    if longestIncreasingRun(1)!=None:
        testLongestIncreasingRun()
        pass
    if nthPalindromicPrime(0)!=None:
        testNthPalindromicPrime()
        pass
    if nthLeftTruncatablePrime(0)!=None:
        testNthLeftTruncatablePrime()
        pass
    if nthPowerfulNumber(1)!=None:
        testNthPowerfulNumber()
        pass
    if isStrobogrammaticNumber(1)!=None:
        testIsStrobogrammaticNumber()
        pass
    if nthHappyNumber(1)!=None:
        testNthHappyNumber()
        pass
    if nthHappyPrime(1)!=None:
        testNthHappyPrime()
        pass
    if nearestKaprekarNumber(1)!=None:
        testNearestKaprekarNumber()
        pass
    if nthCarolPrime(1)!=None:
        testNthCarolPrime()
        pass
    if carrylessAdd(1,1)!=None:
        testCarrylessAdd()
        pass
    if integral(f1,1,1,1)!=None:
        testIntegral()
        pass
    def f(x):return x
    if findZeroWithBisection(f,-1,1,10**-1)!=None:
        testFindZeroWithBisection()
        pass

total=0
testAll()
print()
print('Total Score...',total)