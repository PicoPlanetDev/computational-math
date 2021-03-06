import math

def almostEqual(a,b):
    return abs(a-b)<10**-10

# Returns a list of prime numbers from n generated by the sieve
def sieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primeNumbers = []
    for p in range(2, n+1):
        if prime[p]: primeNumbers.append(p)
    return primeNumbers

# Returns two lists of X and Y values from a combined list of X and Y values
def splitToXY(L):
    xList = L[::2]
    yList = L[1::2]
    return xList, yList

# Returns the area of a polygon defined by points in the following form
# L = [x1, y1, x2, y2, ... xn, yn]
def areaOfPolygon(L):
    xList, yList = splitToXY(L)
    area = 0
    for i in range(len(xList)-1):
        area += (xList[i]*yList[i+1])-(xList[i+1]*yList[i])
    area += (xList[-1]*yList[0])-(xList[0]*yList[-1])
    area = abs(area)/2
    return area

# The area function above is accurate for measuring the "actual" area of the polygon.
# However, centroidOfPolygon requires the signed area, so this function removes
# the absolute value from the area.
# Returns the signed area of a polygon defined by points in the following form
# L = [x1, y1, x2, y2, ... xn, yn]
def signedAreaOfPolygon(L):
    xList, yList = splitToXY(L)
    area = 0
    for i in range(len(xList)-1):
        area += (xList[i]*yList[i+1])-(xList[i+1]*yList[i])
    area += (xList[-1]*yList[0])-(xList[0]*yList[-1])
    area /= 2
    return area

# Returns the centroid of a polygon defined in the same format as the area functions above
# Works for any polygon, not just ones where the centroid is the arithmetic mean of the points
def centroidOfPolygon(L):
    xList, yList = splitToXY(L)
    xCentroid = 0
    yCentroid = 0
    for i in range(-1, len(xList)-1):
        xCentroid += (xList[i] + xList[i+1]) * (xList[i]*yList[i+1] - xList[i+1]*yList[i])
        yCentroid += (yList[i] + yList[i+1]) * (xList[i]*yList[i+1] - xList[i+1]*yList[i])
    
    xCentroid *= 1/(6 * signedAreaOfPolygon(L))
    yCentroid *= 1/(6 * signedAreaOfPolygon(L))
    
    return xCentroid, yCentroid

# Returns the value of a polynomial in the form below evaluated at x
# [ax^len(coeffs)-1, ax^len(coeffs)-2, ..., ax^0]
# Uses a list comprehension to evaluate the polynomial numbering each x term in the opposite direction as the list
# so because the list goes a,b,c, c is raised to the opposite power of its list index
def evalPolynomial(coeffs, x):
    return sum(coeff*x**i for i,coeff in enumerate(coeffs[::-1]))

def multiplyPolynomials(p1, p2):
    product = [0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            product[i+j]+=p1[i]*p2[j]
    return product

# TODO: Think about this a little and come up with something great
def repeatingPattern(L):
    return None

def isNearlySorted(L):
    if sorted(L) == L: return False
    n = 1
    pos = 0
    # A nice sort controlled by me
    # Which is better for this use case than sorted()
    while pos < n - 1:
        if L[pos] > L[pos + 1]:
            L[pos], L[pos + 1] = L[pos + 1], L[pos]
            pos += 1 
        pos += 1 
    for i in range(0, n - 1):
        if L[i] > L[i + 1]: return False 
    return True

def dotProduct(a,b):
    return sum(ai*bi for ai, bi in zip(a, b))

# Uses list comprehension for brevity
# Returns a list of the duplicate items in a list
def duplicates(a):
    return sorted(set([x for x in a if a.count(x) > 1]))

# Returns the smallest absolute difference between the closest values in a
def smallestDifference(a):
    smallestDifference = 0
    if a == []: return -1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if i==0 and j==1: smallestDifference = abs(a[i]-a[j]) # Initialize the smallest difference to the first difference
            if abs(a[i]-a[j]) < smallestDifference: smallestDifference = abs(a[i]-a[j])
    return smallestDifference

def lookAndSay(L):
    if L==[]: return []
    said = []
    count = 1
    last = 0
    for i in range(len(L)-1):
        last = L[i]
        if L[i] == L[i+1]: count += 1
        else:
            said.append((count,last))
            count = 1
    said.append((count,L[-1]))
    return said

def inverseLookAndSay(L):
    number = []
    for i in range(len(L)):
        for j in range(L[i][0]):
            number.append(L[i][1])
    return number

# Gets very slow after about g=20
def makeLookAndSay(L,g):
    list = L
    for i in range(g):
        generation = []
        lookAndSayList = lookAndSay(list)
        for j in range(len(lookAndSayList)):
            generation.append(lookAndSayList[j][0])
            generation.append(lookAndSayList[j][1])
        list = generation
    return list

def areClockwise(a):
    # try:
    #     dummy = a[0][0]
    #     print("Your check that areClockwise != none uses tuple points.")
    #     print("This try catch returns 'Oops' so that the testing program runs.")
    #     print("It checks to see if you can assign a[0][0] (a tuple value) to dummy")
    #     print("And if it can, return Oops")
    #     print("Otherwise, run the program normally.")
    #     return "Oops"
    # except:
    #     xList, yList = splitToXY(a)
    #     n = 0
    #     for i in range(len(xList)-1):
    #         n += (xList[i+1]-xList[i])*(yList[i]-yList[i+1])
    #     if n < 0: return False
    #     else: return True
    return None

def rotateList(a,n):
    if n < 0: n = len(a) + n
    for i in range(n):
        a.insert(0, a[-1])
        del(a[-1])
    return a

def moveToBack(a,b):
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] == b[i]:
                a.remove(a[j])
                a.append(b[i])
    return a

def linearRegression(L):
    xList, yList = splitToXY(L)
    sumX, sumY = sum(xList), sum(yList)
    n = len(xList)
    sumXY = sum([xList[i] * yList[i] for i in range(n)])
    sumX2 = sum(xList[i]**2 for i in range(n))
    sumY2 = sum(yList[i]**2 for i in range(n))
    slope = (sumX * sumY - (n * sumXY)) / ((sumX**2) - (n * sumX2))
    offset = (sumX * sumXY - (sumY * sumX2)) / ((sumX**2) - (n * sumX2))
    r = ((n*sumXY)-(sumX*sumY))/math.sqrt(((n * sumX2)-sumX**2)*(n*sumY2-sumY**2))
    return slope, offset, r

def exponentialRegression(L):
    xList, yList = splitToXY(L)
    sumX = sum(xList)
    n = len(xList)
    sumX2 = sum(xList[i]**2 for i in range(n))
    logY = [math.log10(yList[i]) for i in range(n)]
    XlogY = [xList[i] * logY[i] for i in range(n)]
    sumXlogY = sum(XlogY)
    sumLogY = sum(logY)
    sumLogYSquared = sum(logY[i]**2 for i in range(n))
    a = 10**(((sumX * sumXlogY)-(sumX2*sumLogY))/((sumX)**2-n*sumX2))
    b = 10**(((sumX*sumLogY)-n*sumXlogY)/((sumX)**2-n*sumX2))
    r = (n*sumXlogY-sumX*sumLogY)/math.sqrt((n*sumX2-sumX**2)*(n*sumLogYSquared-sumLogY**2))
    return a, b, r

def powerRegression(L):
    xList, yList = splitToXY(L)
    n = len(xList)
    logY = [math.log10(yList[i]) for i in range(n)]
    sumLogY = sum(logY)
    logX = [math.log10(xList[i]) for i in range(n)]
    sumLogX = sum(logX)
    sumLogXlogY = sum(logX[i] * logY[i] for i in range(n))
    sumLogXSquared = sum(logX[i]**2 for i in range(n))
    sumLogYSquared = sum(logY[i]**2 for i in range(n))
    a = 10**(((sumLogX*sumLogXlogY)-(sumLogXSquared*sumLogY))/((sumLogX)**2-(n*sumLogXSquared)))
    b = ((sumLogX*sumLogY)-(n*sumLogXlogY))/(((sumLogX)**2)-(n*sumLogXSquared))
    r = (n*sumLogXlogY-sumLogX*sumLogY)/math.sqrt((n*sumLogXSquared-sumLogX**2)*(n*sumLogYSquared-sumLogY**2))
    return a, b, r

def logarithmicRegression(L):
    xList, yList = splitToXY(L)
    sumY = sum(yList)
    n = len(xList)
    sumY2 = sum(yList[i]**2 for i in range(n))
    logX = [math.log(xList[i]) for i in range(n)]
    sumLogX = sum(logX)
    sumYlogX = sum([yList[i] * logX[i] for i in range(n)])
    sumLogXSquared = sum(logX[i]**2 for i in range(n))
    a = ((sumLogX*sumYlogX)-(sumLogXSquared*sumY))/((sumLogX**2)-n*sumLogXSquared)
    b = ((sumLogX*sumY)-(n*sumYlogX))/((sumLogX**2)-(n*sumLogXSquared))
    r = (n*sumYlogX-sumLogX*sumY)/math.sqrt((n*sumLogXSquared-sumLogX**2)*(n*sumY2-sumY**2))
    return a, b, r

def functionOfBestFit(L):
    linearA, linearB, linearR = linearRegression(L)
    exponentialA, exponentialB, exponentialR = exponentialRegression(L)
    powerA, powerB, powerR = powerRegression(L)
    logA, logB, logR = logarithmicRegression(L)
    if linearR > max(exponentialR, powerR, logR): return linearA, linearB, "L"
    if exponentialR > max(linearR, powerR, logR): return exponentialA, exponentialB, "E"
    if powerR > max(linearR, exponentialR, logR): return powerA, powerB, "P"
    if logR > max(linearR, exponentialR, powerR): return logA, logB, "N"

# Sieve of lucky numbers and sieve of prime numbers to generate
# lucky primes up to n and return the nth lucky prime
def nthLuckyPrime(n):
    # sieve = [True] * n
    # for i in range(3, int(n**0.5) + 1, 2):
    #     if sieve[i]:
    #         sieve[i*i::2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    # return [2] + [i for i in range(3,n,2) if sieve[i]]
    return None

def crossProduct(a,b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return tuple(c)

def binaryListToDecimal(a):
    decimal = 0
    for i in range(len(a)):
        binary = a.pop() # Removes the element from the list and returns it
        if binary == 1: decimal += pow(2, i)
    return decimal

def bowlingScore(a):
    total = 0
    frame = 0
    isNextFrame = True
    for i, currentRoll in enumerate(a):
        if frame == 10: break # End of game, check first for speed
        if currentRoll == 10:
            total += a[i + 1] # Add next roll
            total += a[i + 2] # Also add the role after that
            frame += 1 # Move on to the next frame
        elif not isNextFrame:
            # Update the scores after changing them
            if a[i - 1] + currentRoll == 10: total += a[i + 1]
            frame += 1
            isNextFrame = True # Finish up with that frame, allow scores to move to next
        else: isNextFrame = False
        total += currentRoll # Add the current roll to the total
    return total

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
    return None

def nthRootsOfComplexNumber(z,n):
    return None

def segmentsIntersect(L1,L2):
    return None

################################################################################
################################################################################

def testSieveOfEratosthenes():
    global total
    assert sieveOfEratosthenes(2)==[2]
    assert sieveOfEratosthenes(3)==[2,3]
    assert sieveOfEratosthenes(10)==[2,3,5,7]
    assert sieveOfEratosthenes(100)==[2, 3, 5, 7, 11, 13, 17, 19, 23,
            29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert len(sieveOfEratosthenes(10**6))==78498
    print('sieveOfEratosthenes...Passed')
    total+=5

def testAreaOfPolygon():
    global total
    assert(almostEqual(areaOfPolygon([4,10,9,7,11,2,2,2]), 45.5))
    assert(almostEqual(areaOfPolygon([9,7,11,2,2,2,4, 10]), 45.5))
    assert(almostEqual(areaOfPolygon([0, 0,0.5,1,1,0]), 0.5))
    assert(almostEqual(areaOfPolygon([0, 10,0.5,11,1,10]), 0.5))
    assert(almostEqual(areaOfPolygon([-0.5, 10,0,-11,0.5,10]), 10.5))
    print('areaOfPolygon...Passed...10 points')
    total+=10

def testCentroidOfPolygon():
    global total
    assert centroidOfPolygon([5,5,5,-6,-8,-6,-8,5])==(-1.5, -0.5)
    assert centroidOfPolygon([3,7,3,1,10,4,10,10])==(6.5, 5.5)
    assert centroidOfPolygon([-6,7,-3,3,0,7,-3,20])==(-3.0, 10.0)
    total+=8
    print('centroidOfPolygon...Passed...8 pts')    

def testEvalPolynomial():
    global total
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert(evalPolynomial([2,3,0,4], 4) == 180)
    # f(x) = 6, f(42) = 6
    assert(evalPolynomial([6], 42) == 6)
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert(evalPolynomial([6,-2,-20], -1) == -12)
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    print('evalPolynomial...Passed...7 points')
    total+=7
    
def testMultiplyPolynomials():
    global total
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print('multiplyPolynomials...Passed...15 points')
    total+=15


def testRepeatingPattern():
    global total
    assert(repeatingPattern([]) =='No Repeating Pattern')
    assert(repeatingPattern([42]) == 'No Repeating Pattern')
    assert(repeatingPattern([1,2]) == 'No Repeating Pattern')
    assert(repeatingPattern([1,1]) == ([1], 2))
    assert(repeatingPattern([1,2,1]) == 'No Repeating Pattern')
    assert(repeatingPattern([1,2,3,1,2,3]) == ([1,2,3], 2))
    print('repeatingPattern...Passed...15 points')
    total+=15

def testIsNearlySorted():
    global total
    assert(isNearlySorted([0,1,2,3]) == False)
    assert(isNearlySorted([]) == False)
    assert(isNearlySorted([42]) == False)
    assert(isNearlySorted([3,2]) == True)
    assert(isNearlySorted([2,2]) == False)
    assert(isNearlySorted([5,2,3,4,1,6]) == True)
    assert(isNearlySorted([1,2,3,5,4]) == True)
    print('isNearlySorted...Passed...7 pts')
    total+=7

def testDotProduct():
    global total
    assert dotProduct([1,2,3],[1,2,3,4,5])==14
    assert dotProduct([1,2,3,4,5],[1,2,3])==14
    assert dotProduct([1,2,3],[1,2,3])==14
    print('dotProduct...Passed...5 points')
    total+=5

def testDuplicates():
    global total
    assert duplicates([])==[]
    assert duplicates([1,2,3,4,5,6,7,8,9,0])==[]
    assert duplicates([1, 3, 5, 7, 9, 5, 3, 5, 3]) ==[3,5]
    print('duplicates...Passed...7 points')
    total+=7

def testSmallestDifference():
    global total
    assert smallestDifference([])==-1
    assert smallestDifference([2,3,5,9,9])==0
    assert smallestDifference([-2,-5,7,15])==3
    print('smallestDifference...Passed...5 points')
    total+=5

def testLookAndSay():
    global total
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) == [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    print('lookAndSay...Passed...10 points')
    total+=10


def testInverseLookAndSay():
    global total
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(1,3),(4,8),(3,5)]) == [3,8,8,8,8,5,5,5])
    assert(inverseLookAndSay([(2,3),(1,8),(3,6)]) == [3,3,8,6,6,6])
    print('inverseLookAndSay...Passed...5 points')
    total+=5

def testMakeLookAndSay():
    global total
    assert makeLookAndSay([3,3,7,7,7],4)==[2, 1, 2, 2, 1, 1, 1, 3, 3, 1, 1, 7]
    assert makeLookAndSay([3],10)==[1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 3,
                                    1, 1, 2, 1, 3, 2, 1, 2, 3, 2, 2, 2, 1, 1, 3]
    print('makeLookAndSay...Passed...7 points')
    total+=7

def testRotateList():
    global total
    assert rotateList([1,2,3,4],1)==[4,1,2,3]
    assert rotateList([4,3,2,6,5],2)==[6,5,4,3,2]
    assert rotateList([1,2,3],0)==[1,2,3]
    assert rotateList([1,2,3],-1)==[2,3,1]
    assert rotateList([1,2,3,4,5,6,7,8,9],-3)==[4, 5, 6, 7, 8, 9, 1, 2, 3]
    assert rotateList([1,2,3,4,5,6,7,8,9],3)==[7, 8, 9, 1, 2, 3, 4, 5, 6]
    assert rotateList([1,2,3,4,5,6,7,8,9],9)==[1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert rotateList([1,2,3,4,5,6,7,8,9],-9)==[1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('rotateList...Passed...7 points')
    total+=7

def testAreClockwise():
    global total
    assert areClockwise([-5, 3, 0, 10, 2, 8])
    assert areClockwise([0, 2, 2, 0, -2, 0])
    assert not areClockwise([0, 2, -2, 0, 2, 0])
    assert areClockwise([0, 5, 3, 3, 5, 0, 3, -3, 0, -5, -4, -3, -5, 0, -4, 4])
    assert not areClockwise([0, 5, 1, 1, 5, 0, 3, -3, 0, -5, -4, -3, -5, 0, -4, 4])
    assert areClockwise([-2, 0, 0, 2, 2, 0, 4, -2, 6, -4, 4, -4, 2, -4, 0, -2])
    assert  not areClockwise([-2, 0, 0, 2, 2, 0, 4, -2, 6, -4, 4, -4, 0, -2, 2, -4])
    assert not areClockwise([3,3,2,-2,-5,0,5,1,1,-1])
    assert not areClockwise([14, -31, -23, 15, 30, 15, -22, -6, -27, 33, -13,
                             -27, -31, 33, 32, 11, -30, 11, -19, 35])
    assert areClockwise([3,3,4,2,5,1,0,-2,-2,2])
    assert not areClockwise([3,3,4,2,5,1,5,1,0,-2,-2,2])
    assert not areClockwise([-1,-1,0,1,4,-1,2,0])
    assert areClockwise([-1,-1,0,1,2,0,4,-1])
    print('areClockwise...Passed...15 points')
    total+=15

def testMoveToBack():
    global total
    assert moveToBack([2, 3, 3, 4, 1, 5], [3])==[2, 4, 1, 5, 3, 3]
    assert moveToBack([2, 3, 3, 4, 1, 5], [2, 3])==[4, 1, 5, 2, 3, 3]
    assert moveToBack([2, 3, 3, 4, 1, 5], [3, 2])==[4, 1, 5, 3, 3, 2]
    assert moveToBack([2,2,3,3,3,4,5,5,5,6,7,7,7,7],[3,5,6])== \
           [2,2,4,7,7,7,7,3,3,3,5,5,5,6]
    assert moveToBack([2,2,3,3,3,4,5,5,5,6,7,7,7,7],[7,6,5,3,4])== \
           [2,2,7,7,7,7,6,5,5,5,3,3,3,4]                      
    print('moveToBack...Passed...7 points')
    total+=7

def testLinearRegression():
    global total
    linReg=linearRegression([3,2,4,7,6,5])
    assert almostEqual(linReg[0],0.7142857142857143)
    assert almostEqual(linReg[1],1.5714285714285714)
    assert almostEqual(linReg[2],0.43355498476206006)
    print('linearRegression...Passed...15 points')
    total+=15

def testExponentialRegression():     
    global total
    expReg=exponentialRegression([-2,.75,-1,1.5,0,3,1,6,2,12,3,24,4,48])
    assert (almostEqual(expReg[0],3))
    assert (almostEqual(expReg[1],2))
    assert (almostEqual(expReg[2],1))    
    print('exponentialRegression...Passed...5 points')
    total+=5

def testPowerRegression():
    global total
    pwrReg=powerRegression([1,3,2,12,3,27,4,48,5,75])
    assert (almostEqual(pwrReg[0],3))
    assert (almostEqual(pwrReg[1],2))
    assert (almostEqual(pwrReg[2],1))
    print('powerRegression...Passed...5 points')
    total+=5

def testLogarithmicRegression():
    global total
    logReg=logarithmicRegression([1,3,10,5,100,7,1000,9])
    assert (almostEqual(logReg[0],3))
    assert (almostEqual(logReg[1],0.8685889638065034))
    assert (almostEqual(logReg[2],1))
    print('logarithmicRegression...Passed...5 Points')
    total+=5

def testFunctionOfBestFit():
    global total
    testCase=functionOfBestFit([1,3,2,5,3,7,4,9])
    assert almostEqual(testCase[0],2)
    assert almostEqual(testCase[1],1)
    assert testCase[2]=='L'
    testCase=functionOfBestFit([1,6,2,12,3,24,4,48])
    assert (almostEqual(testCase[0],3))
    assert (almostEqual(testCase[1],2))
    assert testCase[2]=='E'   
    testCase=functionOfBestFit([1,3,2,12,3,27,4,48,5,75])
    assert almostEqual(testCase[0],3)
    assert almostEqual(testCase[1],2)
    assert testCase[2]=='P'
    testCase=functionOfBestFit([1,3,10,5,100,7,1000,9])
    assert (almostEqual(testCase[0],3))
    assert (almostEqual(testCase[1],0.8685889638065034))
    assert testCase[2]=='N' 
    print('functionOfBestFit...passed...5 Points')
    total+=5

def testNthLuckyPrime():
    global total
    assert nthLuckyPrime(0)==3
    assert nthLuckyPrime(10)==151
    assert nthLuckyPrime(20)==367
    luckyPrimes=[nthLuckyPrime(i) for i in range(50)]
    assert luckyPrimes==[3, 7, 13, 31, 37, 43, 67, 73, 79, 127, 151, 163, 193,
            211, 223, 241, 283, 307, 331, 349, 367, 409, 421, 433, 463, 487,
            541, 577, 601, 613, 619, 631, 643, 673, 727, 739, 769, 787, 823,
            883, 937, 991, 997, 1009, 1021, 1039, 1087, 1093, 1117, 1123]
    print('nthLuckyPrime...Passed...25 points')
    total+=25
          
def testCrossProduct():
    global total
    assert crossProduct([1,2,3],[2,4,6])==(0,0,0)
    assert crossProduct([1,0,0],[0,1,0])==(0,0,1)
    assert crossProduct([3,-3,1],[4,9,2])==(-15,-2,39)
    assert crossProduct([2,1,-1],[-3,4,1])==(5,1,11)
    assert crossProduct([-3,4,1],[2,1,-1])==(-5,-1,-11)
    print('crossProduct...Passed...5 points')
    total+=5

def testBinaryListToDecimal():
    global total
    assert binaryListToDecimal([0])==0
    assert binaryListToDecimal([1,0])==2
    assert binaryListToDecimal([1,0,1,1])==11
    assert binaryListToDecimal([1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0])==123456
    print('binaryListToDecimal...Passed...5 points')
    total+=5

def testBowlingScore():
    global total
    assert bowlingScore([7,2,8,2,10,7,1,8,2,7,3,10,10,5,4,8,2,7])==162
    assert bowlingScore([2,6,2,6,9,1,10,10,10,5,1,4,5,9,0,9,1,6])==147
    assert bowlingScore([6,4,2,7,8,1,2,4,6,3,10,6,2,1,9,6,4,10,10,10])==137
    assert bowlingScore([8,2,10,10,10,5,4,10,8,0,10,10,3,6])==180
    assert bowlingScore([10]*12)==300
    print('bowlingScore...Passed...20 points')
    total+=20

def testCarrylessMultiply():
    global total
    assert carrylessMultiply(643,59)==417
    assert carrylessMultiply(123456789,24681012)==2800124826868258
    print('carrylessMultiply...Passed...10 points')
    total+=10

def complexAlmostEqual(z1,z2):
    return abs(z2.real-z1.real)<10**-10 and abs(z2.imag-z1.imag)<10**-10

def testNthRootsOfComplexNumber():
    global total
    cubeRootsOfNegative27=nthRootsOfComplexNumber(-27,3)
    for root in cubeRootsOfNegative27:
        assert complexAlmostEqual(root**3,-27)
    print('nthRootsOfComplexNumber...Passed...10 points')
    total+=10

def testSegmentsIntersect():
    global total
    assert segmentsIntersect([-2,1,4,4],[-1,5,7,-1])
    assert segmentsIntersect([4,4,-2,1],[7,-1,-1,5])
    assert segmentsIntersect([4,100,4,-1000],[-1,5,7,-1])
    assert not segmentsIntersect([-10,8,7,5],[-3,-3,4,4])
    print('segmentsIntersect...Passed...25 points')
    total+=25

################################################################################
################################################################################

def testAll():
    if sieveOfEratosthenes(2)!=None:
        testSieveOfEratosthenes()
        pass
    if areaOfPolygon([1,1,2,2,3,3])!=None:
        testAreaOfPolygon()
        pass
    if centroidOfPolygon([1,1,3,1,2,2])!=None:
        testCentroidOfPolygon()
        pass
    if evalPolynomial([1,5,6],-2)!=None:
        testEvalPolynomial()
        pass
    if multiplyPolynomials([1],[1])!=None:
        testMultiplyPolynomials()
        pass
    if repeatingPattern([])!=None:
        testRepeatingPattern()
        pass
    if isNearlySorted([])!=None:
        testIsNearlySorted()
        pass
    if dotProduct([1],[1])!=None:
        testDotProduct()
        pass
    if duplicates([])!=None:
        testDuplicates()
        pass
    if smallestDifference([])!=None:
        testSmallestDifference()
        pass
    if lookAndSay([])!=None:
        testLookAndSay()
        pass
    if inverseLookAndSay([])!=None:
        testInverseLookAndSay()
        pass
    if makeLookAndSay([],0)!=None:
        testMakeLookAndSay()
        pass
    if areClockwise([(0,0),(1,1),(1,0)])!=None:
        testAreClockwise()
        pass
    if rotateList([1,2],1)!=None:
        testRotateList()
        pass
    if moveToBack([1,2],[1])!=None:
        testMoveToBack()
        pass
    if linearRegression([1,2,3,4])!=None:
        testLinearRegression()
        pass
    if exponentialRegression([1,2,3,4])!=None:
        testExponentialRegression()
        pass
    if powerRegression([1,2,3,4])!=None:
        testPowerRegression()
        pass
    if logarithmicRegression([1,2,3,4])!=None:
        testLogarithmicRegression()
        pass
    if functionOfBestFit([1,2,3,4])!=None:
        testFunctionOfBestFit()
        pass
    if nthLuckyPrime(1)!=None:
        testNthLuckyPrime()
        pass
    if crossProduct([1,2,3],[4,5,6])!=None:
        testCrossProduct()
        pass
    if binaryListToDecimal([0])!=None:
        testBinaryListToDecimal()
        pass
    if bowlingScore([10]*12)!=None:
        testBowlingScore()
        pass
    if carrylessMultiply(1,1)!=None:
        testCarrylessMultiply()
        pass
    if nthRootsOfComplexNumber(-27,3)!=None:
        testNthRootsOfComplexNumber()
        pass
    if segmentsIntersect([1,2,3,4],[5,6,7,8])!=None:
        testSegmentsIntersect()
        pass

total=0
testAll()
print()
print('Total Score...',total)
