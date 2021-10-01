######################################################################
##       Mathematical Computation Quiz Unit Two     ##################
######################################################################
import math

def almostEqual(x,y):
    return abs(x-y)<10**-10

def sumOfFirstMIntegersDivisibleByN(m,n):
    total = 0
    count = 0
    num = 0
    while count <= m:
        if num%n==0:
            total += num
            count += 1
        num += n
    return total

def largestSumOfAdjacentDigits(n):
    return None

def isPermutation(a,b):
    zero = one = two = three = four = five = six = seven = eight = nine = 0
    zero2 = one2 = two2 = three2 = four2 = five2 = six2 = seven2 = eight2 = nine2 = 0
   
   
    while a>= 1:
        new = kthDigit(a, 0)
        if new == 0: zero = zero + 1
        if new == 1: one = one + 1
        if new == 2: two = two + 1
        if new == 3: three = three + 1
        if new == 4: four = four + 1
        if new == 5: five = five + 1
        if new == 6: six = six + 1
        if new == 7: seven = seven + 1
        if new == 8: eight = eight + 1
        if new == 9: nine = nine + 1
        a = a/10
       
    while b>= 1:
        new = kthDigit(b, 0)
        if new == 0: zero2 = zero2 + 1
        if new == 1: one2 = one2 + 1
        if new == 2: two2 = two2 + 1
        if new == 3: three2 = three2 + 1
        if new == 4: four2 = four2 + 1
        if new == 5: five2 = five2 + 1
        if new == 6: six2 = six2 + 1
        if new == 7: seven2 = seven2 + 1
        if new == 8: eight2 = eight2 + 1
        if new == 9: nine2 = nine2 + 1
        b = b/10
       
    if zero == zero2 and one == one2 and two == two2 and three == three2 and four == four2 and five == five2 and six == six2 and seven == seven2 and eight == eight2 and nine == nine2: return True
    else: return False

def estimateExponentialFunction(x,terms):
    total = 1
    for i in range (terms):
        total = total + ((x**(i+1)) / math.factorial(i+1))
    return total

def sumOfProductsOfAllIntegerPairsLessThanN(n):
    return None

def nthSexyPrime(n):
    return None

def nthSemiprime(n):
    return None

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

# Returns true if n is a prime number
def isPrime(n):
    if (n < 2): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    for factor in range(3,round(n**0.5)+1,2):
        if (n % factor == 0): return False
    return True

def nthCircularPrime(n):
    return None

def nthAbundantNumber(n):
    return None

def harderCannonAiming( initialHeight,targetRange):
    return None


#############################################################################
####  All Test Cases Are Here  ##############################################
#############################################################################

def almostEqual(x,y):
    return abs(x-y)<10**-10

def testNthAbundantNumber():
    assert nthAbundantNumber(0)==12
    assert nthAbundantNumber(10)==56
    assert nthAbundantNumber(231)==945  #First odd abundant Number
    abunds=[nthAbundantNumber(i) for i in range(3,987,7)]
    assert abunds==[24, 56, 84, 108, 140, 174, 200, 224, 260, 288, 318,
                    348, 368, 396, 426, 456, 480, 510, 540, 564, 594, 620,
                    648, 680, 708, 738, 762, 792, 820, 846, 876, 906, 930,
                    954, 984, 1014, 1044, 1074, 1104, 1140, 1164, 1190, 1218,
                    1242, 1280, 1308, 1332, 1360, 1386, 1416, 1446, 1472, 1496,
                    1524, 1560, 1584, 1614, 1644, 1668, 1698, 1722, 1752, 1780,
                    1812, 1842, 1872, 1896, 1926, 1952, 1980, 2002, 2028, 2058,
                    2082, 2118, 2142, 2172, 2200, 2220, 2256, 2288, 2316, 2346,
                    2376, 2406, 2432, 2460, 2484, 2514, 2544, 2568, 2592, 2622,
                    2652, 2682, 2716, 2740, 2760, 2796, 2826, 2850, 2880, 2910,
                    2940, 2968, 2992, 3012, 3040, 3072, 3102, 3136, 3162, 3192,
                    3222, 3248, 3270, 3300, 3328, 3348, 3384, 3408, 3432, 3462,
                    3492, 3520, 3552, 3580, 3608, 3640, 3672, 3702, 3726, 3756,
                    3780, 3808, 3836, 3860, 3888, 3918, 3944, 3972]
    print('nthAbundantNumber...Passed')
            
def testSumOfFirstMIntegersDivisibleByN():
    assert sumOfFirstMIntegersDivisibleByN(100,1)==5050
    assert sumOfFirstMIntegersDivisibleByN(2,2)==6
    assert sumOfFirstMIntegersDivisibleByN(25,6)==1950
    assert sumOfFirstMIntegersDivisibleByN (4,3)==30
    assert sumOfFirstMIntegersDivisibleByN(5*10**5,6)==750001500000
    numbers=[sumOfFirstMIntegersDivisibleByN(10**4,i) for i in range(6,600,28)]
    assert numbers==[300030000, 1700170000, 3100310000, 4500450000,
                     5900590000, 7300730000, 8700870000, 10101010000,
                     11501150000, 12901290000, 14301430000, 15701570000,
                     17101710000, 18501850000, 19901990000, 21302130000,
                     22702270000, 24102410000, 25502550000, 26902690000,
                     28302830000, 29702970000]
    print('sumOfFirstMIntegersDivisibleByN...Passed')
    

def testLargestSumOfAdjacentDigits():
    assert largestSumOfAdjacentDigits(1234567)==13
    assert largestSumOfAdjacentDigits(12345612)==11
    assert largestSumOfAdjacentDigits(12345)==9
    assert largestSumOfAdjacentDigits(12345234)==9
    assert largestSumOfAdjacentDigits(1237845676543)==15
    assert largestSumOfAdjacentDigits(1239987654987634017)==18
    assert [largestSumOfAdjacentDigits(i) for i in range(135798,10**7,315792)] \
           ==[17, 14, 13, 11, 17, 13, 10, 10, 12, 16, 12, 14, 12, 13, 16, 15,
            16, 10, 13, 13, 11, 13, 11, 18, 14, 17, 12, 14,17, 13, 15, 18]
    print('largestSumOfAdjacentDigits...Passed')

def testHarderCannonAiming():
    assert harderCannonAiming(200,11000)==36.29
    assert harderCannonAiming(400,12000)==44.02
    assert harderCannonAiming(0,1000)==2.55
    assert harderCannonAiming(5000,15000)==26.57
    assert [harderCannonAiming(i,10**4) for i in range(5,500,63)]== \
           [31.32, 30.75, 30.19, 29.63, 29.09, 28.54, 28.01, 27.48]
    assert [harderCannonAiming(347,i) for i in range(100,10**4,1257)]== \
           [0.01, 0.01, 0.01, 4.78, 9.46, 13.86, 18.34, 23.24]          
    print('harderCannonAiming...Passed')

def testEstimateExponentialFunction():
    assert estimateExponentialFunction(1,0)==1
    assert estimateExponentialFunction(1,1)==2
    assert estimateExponentialFunction(1,2)==2.5
    assert round(estimateExponentialFunction(.7,4),10)==2.0121708333
    for i in range(-5,6):
        assert almostEqual(estimateExponentialFunction(i,1000),math.exp(i))
    print('estimateExponentialFunction...Passed')

def testNthSemiprime():
    assert nthSemiprime(0)==4
    assert nthSemiprime(10)==33
    assert nthSemiprime(100)==319
    assert nthSemiprime(10**4)==40886
    semis=[nthSemiprime(i) for i in range(61)]
    assert semis==[4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39,
                   46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86,
                   87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 121, 122,
                   123, 129, 133, 134, 141, 142, 143, 145, 146, 155, 158,
                   159, 161, 166, 169, 177, 178, 183, 185, 187]
    print('nthSemiprime...Passed')

def testSumOfProductsOfAllIntegerPairsLessThanN():
    assert sumOfProductsOfAllIntegerPairsLessThanN(1)==0
    assert sumOfProductsOfAllIntegerPairsLessThanN(2)==1
    assert sumOfProductsOfAllIntegerPairsLessThanN(3)==7
    assert sumOfProductsOfAllIntegerPairsLessThanN(4)==25
    assert sumOfProductsOfAllIntegerPairsLessThanN(5)==65
    assert sumOfProductsOfAllIntegerPairsLessThanN(100)==12415425
    assert sumOfProductsOfAllIntegerPairsLessThanN(1234)==289691449125
    assert [sumOfProductsOfAllIntegerPairsLessThanN(i)
            for i in range(7,10**3,74)]==\
            [266, 5335740, 71836765, 342750025, 1051281932, 2520598626,
             5163825975, 9484049575, 16074314750, 25617626552, 38886949761,
             56745208885, 80145288160, 110130031550]
    print('sumOfProductsOfAllIntegerPairsLessThanN...Passed')
    
def testNthSexyPrime():
    assert nthSexyPrime(0)==5
    sexy=[nthSexyPrime(i) for i in range(50)]
    assert sexy==[5, 7, 11, 13, 17, 23, 31, 37, 41, 47, 53, 61, 67, 73, 83,
                  97, 101, 103, 107, 131, 151, 157, 167, 173, 191, 193, 223,
                  227, 233, 251, 257, 263, 271, 277, 307, 311, 331, 347, 353,
                  367, 373, 383, 433, 443, 457, 461, 503, 541, 557, 563]
    print('nthSexyPrime...Passed')

def testNthCircularPrime():
    assert nthCircularPrime(0)==2
    circles=[nthCircularPrime(i) for i in range(40)]
    assert circles==[2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113,
                     131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991,
                     1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939,
                     19391, 19937, 37199, 39119, 71993, 91193]
    print('nthCircularPrime...Passed')

def testIsPermutation():
    values=[23145, 21534, 38111, 19888, 20685, 41532, 43493, 35142, 43215,
            17278, 45312, 21354, 24531, 17424, 24135, 26817, 18046, 23865,
            40864, 42773, 42153, 23415, 12354, 41713, 12453, 24083, 35421,
            16814, 23514, 19668, 25134, 26308, 22879, 51243, 14463, 41326,
            17742, 13452, 18872, 51432, 13254, 23154, 39215, 25314, 53142,
            29958, 34512, 43251, 32130, 27577, 30371, 37960, 33554, 39314,
            38610, 42531, 12345, 32415, 40511, 11151, 31542, 10036, 41523,
            53241, 14253, 45231, 32145, 42377, 20023, 24747, 54321, 53412,
            19786, 54123, 31590, 34251, 28053, 18654, 21435, 32514, 17485,
            13542, 13996, 21345, 25341, 25186, 10431, 31425, 12435, 25431,
            13425, 25272, 25918, 35124, 45132, 14966, 42038, 22402, 53124,
            18977, 51324, 24315, 40606, 29131, 12630, 25759, 19363, 52134,
            31500, 20085, 12667, 16970, 15432, 31245, 41253, 43375, 32783,
            11146, 33306, 54231, 24153, 43125, 32154, 43152, 41235, 36573,
            20575, 22357, 34152, 54312, 29755, 23438, 34521, 34215, 15234,
            37463, 11884, 16981, 32578, 41588, 25143, 45321, 14235, 35412,
            31254, 39696, 40562, 34125, 15390, 34973, 21453, 14352, 19695,
            42102, 42135, 43512, 21543, 42712, 37200, 42351, 19181, 54132,
            37182, 11318, 52314, 16857, 33827, 25413, 23451, 27736, 36693,
            51342, 35253, 31221, 52143, 41025, 13245, 15324, 52341, 30338,
            35241, 43521, 42659, 30416, 11172, 12534, 30901, 32541, 10435,
            14532, 41145, 32664, 24351, 15243, 31524, 22012, 18057, 42194,
            23541, 41531, 42315, 32451, 12814, 41352, 41325, 21538, 45213,
            13524, 29407, 24513, 38166, 10845, 51234, 15342, 32765, 24251,
            40435, 15423, 20064, 13491, 24416, 52413, 31452, 32340, 12543,
            52431, 35214, 14523, 14325, 51423, 43645, 31241, 33707, 43032,
            54213, 53421, 11183, 53214, 45123, 42513]
    assert [isPermutation(values[2*i],values[2*i+1]) for i in range(len(values)//2)]== \
    [True, False, False, False, False, True, False, False, False, False, True, False,
     False, False, False, False, False, False, False, False, True, False, False, True,
     False, False, False, False, True, False, False, True, True, False, False, True,
     False, False, False, True, False, False, False, False, True, False, False, False,
     False, False, True, False, False, False, False, False, True, False, False, False,
     True, True, False, False, True, False, True, False, False, False, True, True,
     False, False, False, True, False, True, False, False, False, False, False, False,
     False, False, False, False, True, False, True, False, False, False, False, False,
     True, False, False, False, True, False, False, True, False, False, True, False,
     False, False, False, False, True, True, True, False, False, True, False, True]
    print('isPermutation...Passed')

def testAll():
    if nthAbundantNumber(1)!=None:
        testNthAbundantNumber()
        pass
    if sumOfFirstMIntegersDivisibleByN(1,1)!=None:
        testSumOfFirstMIntegersDivisibleByN()
        pass
    if largestSumOfAdjacentDigits(1)!=None:
        testLargestSumOfAdjacentDigits()
        pass
    if harderCannonAiming(1,1)!=None:
        testHarderCannonAiming()
        pass
    if estimateExponentialFunction(1,1)!=None:
        testEstimateExponentialFunction()
        pass
    if nthSemiprime(0)!=None:
        testNthSemiprime()
        pass
    if sumOfProductsOfAllIntegerPairsLessThanN(1)!=None:
        testSumOfProductsOfAllIntegerPairsLessThanN()
        pass
    if nthSexyPrime(0)!=None:
        testNthSexyPrime()
        pass
    if nthCircularPrime(0)!=None:
        testNthCircularPrime()
    if isPermutation(1,1)!=None:
        testIsPermutation()
print('SOLUTIONS*********')
import time
start=time.time()
testAll()
print(time.time()-start)
