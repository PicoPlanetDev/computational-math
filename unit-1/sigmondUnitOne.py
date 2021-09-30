############################## INFO ####################################
##    Unit One Starting Point                                         ##
##    DO NOT CHANGE THE NAMES OF THE PROGRAMS!!!!!                    ##
##    Replace None with your code.                                    ##
##    If you don't submit one of these programs, leave None in place. ##
##    almostEqual is provided                                         ##
########################################################################

import math

# Replacement for == that accounts for floating point errors
def almostEqual(x,y):
    return abs(x-y)<10**-9

# Determines if n is a square number
def isPerfectSquare(n):
    if n<0:return False
    return n**.5%1==0

# Determines if f is a factor of n
def isFactor(f,n):
    if f==0: return False
    if n%f!=0: return False
    if n==0: return True
    if n%f==0: return True
    
# Determines if m is a multiple of n
def isMultiple(n,m):
    return isFactor(n,m)

# Returns the kth digit of n counting from the right  
def kthDigit(n, k):
    return int(abs(n) // (10**k) % 10)

# Distance formula
def distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

# Determines if the three side lengths form a triangle
def isLegalTriangle(s1,s2,s3):
    if s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1: return True
    else: return False

# Determines if the points form a legal triangle that also has a right angle
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x1, y1, x3, y3)
    if not isLegalTriangle(s1,s2,s3): return None
    if s1 > s2 and s1 > s3:
        if almostEqual(s2**2+s3**2,s1**2):
            return True
    elif s2 > s1 and s2 > s3:
        if almostEqual(s1**2 + s3**2,s2**2):
            return True
    elif s3 > s2 and s3 > s1:
        if almostEqual(s1**2 + s2**2,s3**2):
            return True
    else: return False

# Uses Heron's formula to determine the area of a triangle with three points
def triangleAreaByCoordinates(x1,y1,x2,y2,x3,y3):
    if not isLegalTriangle(distance(x1, y1, x2, y2),distance(x2, y2, x3, y3),distance(x1, y1, x3, y3)): return False
    return abs((x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)/2)

# Returns the nth number in the Fibonacci sequence
def nthFibonacci(n):
    if n==0 or n==1: return 1
    phi=(math.sqrt(5)+1)/2
    return round(((math.pow(phi,n+1))-(math.pow(-(1-phi),n+1)))/math.sqrt(5))

# Returns the excess amount of fabric after fabricInches is cut off of a 36 inch piece
def fabricExcess(fabricInches):
    if fabricInches==0: return 0
    if isMultiple(36,fabricInches): return 0
    else: return 36-fabricInches%36

# Returns the nearest bus stop, which are on every 8th street
def nearestBusStop(street):
    floor = math.floor(street/8)*8
    ceil = math.ceil(street/8)*8
    if abs(street-floor)<abs(street-ceil): return floor
    elif abs(street-floor)>abs(street-ceil): return ceil
    elif almostEqual(abs(street-floor),abs(street-ceil)): return floor

# Determines if two circles intersect given their centers and radii
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    minDistance = distance(x1,y1,x2,y2) - (r1+r2)
    if minDistance > 0: return False
    elif minDistance <= 0: return True

# Finds the nearest odd to any number
def nearestOdd(n):
    f = int(math.ceil(n))
    if almostEqual(f%2,0): return f-1 
    else: return f

# Returns the number of cartons are necessary to package eggs number of eggs if each carton holds 12 eggs
def eggCartons(eggs):
    return int(math.ceil(eggs/12))

# Returns the number located in row row and column col of pascal's triangle
def pascalsTriangleValue(row,col):
    return int((math.factorial(row)) / ((math.factorial(col)) * math.factorial(row - col)))

# Determines if n is a perfect cube
def isPerfectCube(n):
    n = abs(n)
    return almostEqual(round(n**(1/3))**3, n)

# Determines if n is an even, positive integer
def isEvenPositiveInt(n):
    # Tries to convert n to an int, catching an exception if it fails and returning false before determining if it's even and positive
    try: int(n)
    except: return False
    if n>0 and almostEqual(n%2,0): return True
    return False

# Returns the Fahrenheit temperature of the paramaeter Celsius degrees
def celsiusToFahrenheit(degrees):
    return degrees*(9/5)+32

# Returns the Celsius temperature of the paramaeter Fahrenheit degrees
def fahrenheitToCelsius(degrees):
    return (degrees-32)*(5/9)

# Determines if three points are collinear using their area if arranged as a triangle
def areCollinear(x1, y1, x2, y2, x3, y3):
    if almostEqual(triangleAreaByCoordinates(x1,y1,x2,y2,x3,y3),0): return True
    else: return False

# Returns the number of pool balls that fin in rows number of rows according to the layout below:
# \o o o/
#  \o o/
#   \o/
def numberOfPoolBalls(rows):
    return (rows**2+rows)/2

# Returns the number of rows necessary to fit balls number of balls according to the layout below:
# \o o o/
#  \o o/
#   \o/
def numberOfPoolBallRows(balls):
    return round(math.sqrt(balls*2))

# Solves the sphere surface area equation for radius r then passes result into sphere volume equation for radius r
def sphereVolumeFromSurfaceArea(surfaceArea):
    r = (1/2)*math.sqrt(surfaceArea/math.pi)
    v = (4/3)*(math.pi)*(r**3)
    return v

# setKthDigit implementation using strings
# def setKthDigit(n, k, d):
#     n = str(n)[::-1] # reverse the string
#     n = n[:k] + str(d) + n[k+1:] # replace the kth digit with d
#     return int(n[::-1]) # return the string after it has been reversed back to normal

# Replaces the kth digit k of a number n with the digit d returning the result
def setKthDigit(n, k, d):
    return n-((n//10**k)%10*10**k)+(10**k*d)

# Returns the number of times that the cosine function crosses zero in the interval [0,r]
def cosineZerosCount(r):
    if (r<0): return 0
    else: return int((abs(r)//(math.pi/2) - abs(r)//math.pi))

# Returns the time it takes to go upstream in the river cruise according the the linked problem in the problem set document
def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    return ((totalDistance)/((totalDistance/totalTime)+((totalDistance/totalTime)**2+4*riverCurrent**2)**0.5-2*riverCurrent)) 

# Determines if two rectangles overlap given their top left corners and width and height
def rectanglesOverlap(l1, t1, w1, h1, l2, t2, w2, h2):
    if(((l2>l1)and(l2>l1+w1)) or ((l1>l2)and(l1>l2+w2)) or ((t2>t1)and(t2>t1+h1)) or ((t1>t2)and(t1>t2+h2))): return False
    else: return True

# Determines if two lines in y=mx+b intersect, returning their x value of the point of intersection if they do
def lineIntersection(m1, b1, m2, b2):
    if (m1==m2): return None
    else: return(b2-b1)/(m1-m2)

# Returns the area of a triangle given its three sides
def triangleArea(s1, s2, s3):
    p = (s1+s2+s3)/2
    return math.sqrt(p*(p-s1)*(p-s2)*(p-s3))

# Returns the trianglular area surrounded by three intersecting lines
def threeLinesArea(m1, b1, m2, b2, m3, b3):
    if(lineIntersection(m1, b1, m2, b2)==None or lineIntersection(m2, b3, m3, b3)==None or lineIntersection(m1, b1, m3, b3)==None): return 0
    else:
        x1=lineIntersection(m1, b1, m2, b2)
        x2=lineIntersection(m2, b2, m3, b3)
        x3=lineIntersection(m1, b1, m3, b3)
        y1=m1*lineIntersection(m1, b1, m2, b2)+b1
        y2=m2*lineIntersection(m2, b2, m3, b3)+b2
        y3=m3*lineIntersection(m1, b1, m3, b3)+b3
        return triangleArea(distance(x1,y1,x2,y2),distance(x2,y2,x3,y3),distance(x1,y1,x3,y3))

# Finds the cubic roots of a cubic function in the form of ax^3+bx^2+cx+d=0
def findCubicRoots(a,b,c,d):
    p=-b/(3*a)
    q=p**3+(b*c-3*a*d)/(6*a**2)
    r=c/(3*a)
    i=(q**2+(r-p**2)**3)**(1/2)
    iOnly=i-i.real
    x1=round(((q+iOnly)**(1/3)+(q-iOnly)**(1/3)+p).real)
    x2=round(((-b-x1*a+(b**2-4*a*c-2*a*b*x1-3*a**2*x1**2)**.5)/(2*a)).real)
    x3=round(((-b-x1*a-(b**2-4*a*c-2*a*b*x1-3*a**2*x1**2)**.5)/(2*a)).real)
    smallest=min(x1,x2,x3)
    largest=max(x1,x2,x3)
    mid=x1+x2+x3-smallest-largest
    return(smallest,mid,largest)

# Interpolates between two colors given in 9 decimal long ints with midpoints number of intermediate colors and returns the interpolated color with index n
def colorBlender(rgb1,rgb2,midpoints,n):
    if n<0 or n>midpoints: return "Error" # Return error if the parameters are unreasonable

    # Get the rgb values of the two colors and store them seperately
    b1 = kthDigit(rgb1,0) + kthDigit(rgb1,1)*10 + kthDigit(rgb1,2)*100
    g1 = kthDigit(rgb1,3) + kthDigit(rgb1,4)*10 + kthDigit(rgb1,5)*100
    r1 = kthDigit(rgb1,6) + kthDigit(rgb1,7)*10 + kthDigit(rgb1,8)*100
    b2 = kthDigit(rgb2,0) + kthDigit(rgb2,1)*10 + kthDigit(rgb2,2)*100
    g2 = kthDigit(rgb2,3) + kthDigit(rgb2,4)*10 + kthDigit(rgb2,5)*100
    r2 = kthDigit(rgb2,6) + kthDigit(rgb2,7)*10 + kthDigit(rgb2,8)*100

    # Calculate the difference between the corresponding rgb values
    rDiff = r2-r1
    gDiff = g2-g1
    bDiff = b2-b1

    # Not well named, I tried to do this differently, but it didn't work
    # Anyway, this calculates the amount that needs to be added to each color
    rInterval = round(rDiff * n /(midpoints+1))
    gInterval = round(gDiff *n /(midpoints+1))
    bInterval = round(bDiff *n /(midpoints+1))

    # Add the "intervals" to the rgb values and use proper powers of 10 to place them correctly in the 9 digit int
    rgbOut = ((r1+(rInterval))*1000000)+((g1+(gInterval))*1000)+(b1+bInterval)
    return rgbOut

# Returns the area of a quadrilateral given its four corners
def quadrilateralArea(x1, y1, x2, y2, x3, y3, x4, y4):
    return 0.5*abs((x1*y2)+(x2*y3)+(x3*y4)+(x4*y1)-(y1*x2)-(y2*x3)-(y3*x4)-(y4*x1)) # I doubt that this is Bretschneider's formula but it works by splitting the quadrilateral into two triangles and then using the triangle area formula

# Classifies a quadrilateral
def isSpecialQuadrilateral(x1,y1,x2,y2,x3,y3,x4,y4):
    def dot(vector1X, vector1Y, vector2X, vector2Y):
        dot = vector1X*vector2X + vector1Y*vector2Y
        return dot
    def angleBetween(vector1X, vector1Y, vector2X, vector2Y):
        normalVector1X = vector1X / math.sqrt(vector1X**2 + vector1Y**2)
        normalVector1Y = vector1Y / math.sqrt(vector1X**2 + vector1Y**2)
        normalVector2X = vector2X / math.sqrt(vector2X**2 + vector2Y**2)
        normalVector2Y = vector2Y / math.sqrt(vector2X**2 + vector2Y**2)
        return math.acos(dot(normalVector1X, normalVector1Y, normalVector2X, normalVector2Y))

    aLength = distance(x1,y1,x2,y2)
    bLength = distance(x2,y2,x3,y3)
    cLength = distance(x3,y3,x4,y4)
    dLength = distance(x4,y4,x1,y1)

    aVectorX = x2-x1
    aVectorY = y2-y1
    bVectorX = x3-x2
    bVectorY = y3-y2
    cVectorX = x4-x3
    cVectorY = y4-y3
    dVectorX = x1-x4
    dVectorY = y1-y4

    angle1 = angleBetween(aVectorX, aVectorY, dVectorX, dVectorY)
    angle2 = angleBetween(aVectorX, aVectorY, bVectorX, bVectorY)
    angle3 = angleBetween(bVectorX, bVectorY, cVectorX, cVectorY)
    angle4 = angleBetween(cVectorX, cVectorY, dVectorX, dVectorY)

    if almostEqual(aLength,bLength) and almostEqual(aLength,cLength) and almostEqual(aLength,dLength) and almostEqual(angle1, math.pi/2) and almostEqual(angle2,math.pi/2) and almostEqual(angle3,math.pi/2) and almostEqual(angle4,math.pi/2):
        return "Square"
    if almostEqual(aLength,bLength) and almostEqual(aLength, cLength) and almostEqual(aLength,dLength):
        return "Rhombus"
    if almostEqual(aLength,cLength) and almostEqual(bLength,dLength) and almostEqual(angle1, math.pi/2) and almostEqual(angle2,math.pi/2) and almostEqual(angle3,math.pi/2) and almostEqual(angle4,math.pi/2):
        return "Rectangle"
    if almostEqual(aLength,cLength) and almostEqual(bLength,dLength):
        return "Parallelogram"
    if almostEqual(angle1+angle4,math.pi) or almostEqual(angle2+angle3,math.pi) or almostEqual(angle3+angle4,math.pi) or almostEqual(angle1+angle2,math.pi) or almostEqual(angle1+angle3,math.pi) or almostEqual(angle2+angle4,math.pi):
        return "Trapezoid"
    if (almostEqual(aLength,dLength) and almostEqual(bLength,cLength)) or (almostEqual(aLength,bLength) and almostEqual(cLength,dLength)):
        return "Kite"
    return "Not a Special Quadrilateral"

#############################################################################
##DO NOT ALTER ANYTHING BELOW THIS LINE
#############################################################################
def testisPerfectSquare():
    global total
    assert isPerfectSquare(1)==True
    assert isPerfectSquare(16)==True
    assert isPerfectSquare(1234**2)==True
    assert isPerfectSquare(1234**2+.0000001)==False
    assert isPerfectSquare(3)==False
    assert isPerfectSquare(-4)==False
    z=[round((i/10)**2) for i in range(0,1000,44)]
    assert [isPerfectSquare(item) for item in z]== \
        [True, False, False, False, False, True, False, False, False, False,
         True, False, False, False, False, True, False, False, False, False,
         True, False, False]       
    total+=5
    print('isPerfectSquare...Passed...5 pts')

def testIsFactor():
    global total
    assert isFactor(1,1)==True
    for i in range(-99,99,2):
        assert isFactor(i,0)==True
    assert isFactor(2,10)==True
    assert isFactor(-5,25)==True
    assert isFactor(2,11)==False
    assert isFactor(0,1)==False
    assert isFactor(0,0)==False
    assert isFactor(-2,-11)==False
    assert isFactor(10,2)==False
    assert [isFactor(item,2400) for item in [0.4*i for i in range(100)]]== \
        [False, False, False, False, False, True, False, False, False, False,
         True, False, False, False, False, True, False, False, False, False,
         True, False, False, False, False, True, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, True, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False]
    total+=5
    print('isFactor...Passed...5 pts')
           
def testIsMultiple():
    global total
    assert isMultiple(1,1)==True
    for i in range(-99,99,2):
        assert isMultiple(i,0)==True
    assert isMultiple(1,25)==True
    assert isMultiple(2,10)==True
    assert isMultiple(13,13*33)==True
    assert isMultiple(2,1)==False
    assert isMultiple(0,1)==False
    assert isMultiple(5,2)==False
    assert isMultiple(1231,24)==False
    assert [isMultiple(item,1600) for item in [0.4*i for i in range(100)]]== \
        [False, False, False, False, False, True, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, True, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False]
    total+=5
    print('isMultiple...Passed...5 pts')

def testKthDigit():
    global total
    assert kthDigit(0,0)==0
    assert kthDigit(789,0)==9
    assert kthDigit(789,1)==8
    assert kthDigit(789,2)==7
    assert kthDigit(789,3)==0
    assert kthDigit(-789,2)==7
    testNum='7215512594525925369399067120132827489452466667934752569670510688999956219779712263640719670202924722'
    for i in range(len(testNum)):
        assert int(testNum[i])==kthDigit(int(testNum),len(testNum)-i-1)
    total+=8
    print('kthDigit...Passed...8 pts')
    
def testDistance():
    global total
    assert almostEqual(distance(0,0,3,4),5)==True
    assert almostEqual(distance(0,0,3,5),5.830951894845301)==True
    assert almostEqual(distance(-2,-5,1,0),5.830951894845301)==True
    assert distance(0,0,0,0)==0
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    assert(almostEqual(distance(20, 20, 23, 220), 200.02249873451737))
    import random
    z=[random.randrange(-1000,1000) for i in range(1000)]
    for i in range(len(z)//4):
        assert almostEqual(distance(z[0],z[1],z[2],z[3]),((z[2]-z[0])**2+(z[3]-z[1])**2)**.5)
    total+=5
    print('distance...Passed...5 pts')

def testIsLegalTriangle():
    global total
    assert(isLegalTriangle(3, 4, 5))
    assert(isLegalTriangle(5, 4, 3))
    assert(isLegalTriangle(3, 5, 4))
    assert(isLegalTriangle(0.3, 0.4, 0.5))
    assert isLegalTriangle(3, 4, 7)==False
    assert isLegalTriangle(7, 4, 3)==False
    assert isLegalTriangle(3, 7, 4)==False
    assert isLegalTriangle(5, -3, 1)==False
    assert isLegalTriangle(-3, -4, -5)==False
    z=[533, 83, 363, 477, 247, 209, 938, 379, 536, 14, 95, 314, 302, 296, 835,
       139, 509, 726, 433, 504, 312, 385, 139, 36, 809, 711, 299, 974, 951, 608,
       127, 926, 767, 601, 954, 465, 5, 232, 846, 642, 677, 14, 879, 576, 325,
       625, 984, 951, 494, 783, 97, 556, 548, 720, 842, 816, 474, 71, 499, 392,
       16, 784, 552, 563, 882, 63, 694, 307, 557, 678, 203, 378, 534, 682, 38,
       68, 788, 491, 275, 305, 528, 647, 220, 980, 845, 857, 233, 580, 46, 310,
       971, 673, 555, 425, 157, 90, 673, 879, 620]
    assert [isLegalTriangle(z[i],z[i+1],z[i+2]) for i in range(0,99,3)]== \
          [False, False, False, False, False, False, True, False, True, True,
           False, True, False, False, True, True, False, True, True, False,
           False, False, True, False, False, False, True, False, True, False,
           True, False, True] 
    total+=5
    print('isLegalTriangle...Passed...5 pts')

def testIsRightTriangle():
    global total
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert not isRightTriangle(1, 0, 0, 3, 4, 0)
    z=[9, 5, 5, 7, 1, 5, 7, 2, 7, 6, 9, 6, 3, 8, 8, 8, 7, 2, 7, 6, 2, 6, 8, 1,
       8, 9, 7, 5, 9, 1, 9, 4, 3, 4, 9, 2, 9, 8, 5, 3, 5, 6, 3, 3, 7, 8, 9, 5,
       3, 3, 3, 3, 6, 3, 7, 4, 2, 4, 9, 8, 3, 2, 5, 2, 6, 9, 2, 7, 7, 7, 1, 1,
       2, 5, 1, 9, 8, 8, 7, 7, 4, 5, 7, 7, 4, 7, 9, 4, 6, 7, 8, 9, 7, 8, 3, 1,
       6, 1, 9, 7, 6, 1, 7, 4, 1, 9, 1, 1, 7, 5, 9, 8, 1, 3, 8, 7, 4, 2, 8, 1]
    assert [isRightTriangle(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5]) \
            for i in range(len(z)-6)]== \
        [False, False, False, False, False, False, True, False, False, False,
         False, False, False, True, False, False, True, False, False, True,
         False, False, False, False, False, False, False, False, True, True,
         True, True, False, False, False, False, False, False, True, False,
         False, False, False, False, False, False, False, True, False, False,
         False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, True, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, True, False, False, False,
         False, False, False, False, False, True, False, False, False, False,
         False, False, False, False, False, True, False, False, False, False,
         False, False, False, False]
    total+=5
    print('isRightTriangle...Passed...5 pts')

def testTriangleAreaByCoordinates():
    global total
    assert almostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16)
    assert almostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250)
    assert almostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),4*3**.5)
    assert almostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39)
    assert almostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20)
    assert almostEqual(triangleAreaByCoordinates(-23,14,234,-876,1654,-99),731744.5)
    z=[9, 5, 5, 7, 1, 5, 7, 2, 7, 6, 9, 6, 3, 8, 8, 8, 7, 2, 7, 6, 2, 6, 8, 1,
       8, 9, 7, 5, 9, 1, 9, 4, 3, 4, 9, 2, 9, 8, 5, 3, 5, 6, 3, 3, 7, 8, 9, 5,
       3, 3, 3, 3, 6, 3, 7, 4, 2, 4, 9, 8, 3, 2, 5, 2, 6, 9, 2, 7, 7, 7, 1, 1,
       2, 5, 1, 9, 8, 8, 7, 7, 4, 5, 7, 7, 4, 7, 9, 4, 6, 7, 8, 9, 7, 8, 3, 1,
       6, 1, 9, 7, 6, 1, 7, 4, 1, 9, 1, 1, 7, 5, 9, 8, 1, 3, 8, 7, 4, 2, 8, 1]
    y=[8.0, 2.0, 12.0, 9.0, 12.0, 3.0, 4.0, 12.0, 2.0, 6.0, 5.0, 1.0, 15.0, 3.0,
       2.0, 15.0, 10.0, 12.0, 12.5, 15.0, 24.0, 2.5, 4.0, 6.0, 6.0, 4.0, 3.0, 12.0,
       9.0, 9.0, 6.0, 6.0, 18.0, 4.0, 12.0, 10.0, 6.0, 5.0, 3.0, 3.0, 1.0, 13.0,
       11.0, 12.0, 11.0, 6.0, False, 3.0, False, False, 1.5, 0.5, 2.5, 3.5, 10.0,
       14.0, 9.0, 14.0, 6.0, 3.0, 7.0, 3.5, 13.0, 13.5, 5.0, 6.0, 15.0, 18.0, 9.0,
       1.0, 4.0, 16.0, 13.5, 1.5, 4.0, 1.0, 0.5, 4.5, False, False, 3.0, 5.0, 4.5,
       7.5, 3.0, 1.5, 6.0, 3.5, False, 4.5, 1.5, 15.5, 10.5, 10.5, 9.0, 9.0, False,
       6.0, 1.5, 16.5, 11.5, 15.0, 24.0, 15.0, 24.0, 20.0, 5.0, 19.0, 7.0, 9.5, 1.5,
       4.0, 9.5, 2.0]
    assert y==[round(triangleAreaByCoordinates(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5]),1)
               if triangleAreaByCoordinates(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5])!=False
               else False for i in range(len(z)-6)]
    total+=6
    print('triangleAreaByCoordinates...Passed...6 pts')

def testNthFibonacci():
    global total
    fibs=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
          2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
          317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
          14930352, 24157817, 39088169, 63245986, 102334155, 165580141,
          267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073,
          4807526976, 7778742049, 12586269025]
    assert fibs==[nthFibonacci(i) for i in range(50)]
    total+=7
    print('nthFibonacci...Passed...7 pts')

def testFabricExcess():
    global total
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(almostEqual(fabricExcess(35.5), 0.5))
    assert(almostEqual(fabricExcess(36.5), 35.5))
    assert [fabricExcess(i*36) for i in range(20)]==[0]*20
    z=[28.25, 4.14, 244.49, 198.69, 0.58, 46.09, 192.42, 64.96, 509.49, 543.36,
       104.53, 274.82, 415.99, 19.6, 103.16, 230.91, 511.9, 49.25, 73.87, 40.98,
       224.09, 273.86, 61.4, 250.92, 707.24, 215.96, 243.36, 540.03, 910.4,
       297.82, 566.8, 122.92, 80.06, 190.24, 58.75, 111.55, 295.6, 409.39,
       494.78, 345.18, 425.1, 656.8, 23.44, 71.74, 142.91, 430.43, 294.45,
       70.12, 23.06, 246.71, 18.06, 643.8, 794.0, 459.16, 35.5, 18.81, 160.26,
       48.92, 140.25, 156.96, 199.29, 108.3, 469.64, 171.58, 2.39, 621.68,
       144.89, 5.0, 359.45, 331.69, 61.98, 19.6, 202.18, 319.43, 6.88, 702.71,
       474.46, 404.13, 74.0, 493.41, 544.1, 547.72, 362.01, 526.1, 161.14,
       369.79, 309.66, 453.09, 4.13, 78.5, 27.8, 97.3, 162.72, 231.99, 232.43,
       534.33, 66.4, 48.13, 651.69, 497.22]
    assert [round(fabricExcess(item),2) for item in z]== \
           [7.75, 31.86, 7.51, 17.31, 35.42, 25.91, 23.58, 7.04, 30.51, 32.64,
            3.47, 13.18, 16.01, 16.4, 4.84, 21.09, 28.1, 22.75, 34.13, 31.02,
            27.91, 14.14, 10.6, 1.08, 12.76, 0.04, 8.64, 35.97, 25.6, 26.18,
            9.2, 21.08, 27.94, 25.76, 13.25, 32.45, 28.4, 22.61, 9.22, 14.82,
            6.9, 27.2, 12.56, 0.26, 1.09, 1.57, 29.55, 1.88, 12.94, 5.29,
            17.94, 4.2, 34.0, 8.84, 0.5, 17.19, 19.74, 23.08, 3.75, 23.04,
            16.71, 35.7, 34.36, 8.42, 33.61, 26.32, 35.11, 31.0, 0.55, 28.31,
            10.02, 16.4, 13.82, 4.57, 29.12, 17.29, 29.54, 27.87, 34.0, 10.59,
            31.9, 28.28, 33.99, 13.9, 18.86, 26.21, 14.34, 14.91, 31.87, 29.5,
            8.2, 10.7, 17.28, 20.01, 19.57, 5.67, 5.6, 23.87, 32.31, 6.78]
    total+=5
    print('fabricExcess...Passed...5 pts')
    
def testNearestBusStop():
    global total
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    assert(nearestBusStop(204) == 200)
    assert(nearestBusStop(205) == 208)
    x=[241, 80, 121, 190, 59, 13, 232, 169, 122, 4, 160, 61, 44, 190, 190, 169,
       142, 97, 111, 156, 135, 104, 111, 181, 99, 97, 172, 120, 164, 234, 113,
       107, 122, 1, 117, 193, 117, 118, 85, 92, 237, 65, 56, 103, 135, 188, 152,
       5, 23, 213, 205, 98, 153, 31, 172, 150, 247, 196, 155, 30, 213, 208, 237,
       129, 34, 144, 236, 72, 37, 25, 184, 4, 106, 217, 229, 230, 180, 66, 169,
       103, 5, 149, 56, 223, 165, 146, 94, 109, 55, 193, 232, 140, 77, 152, 181,
       173, 18, 166, 24, 92]
    z=[nearestBusStop(item) for item in x]
    assert z== \
        [240, 80, 120, 192, 56, 16, 232, 168, 120, 0, 160, 64, 40, 192, 192,
         168, 144, 96, 112, 152, 136, 104, 112, 184, 96, 96, 168, 120, 160, 232,
         112, 104, 120, 0, 120, 192, 120, 120, 88, 88, 240, 64, 56, 104, 136,
         184, 152, 8, 24, 216, 208, 96, 152, 32, 168, 152, 248, 192, 152, 32,
         216, 208, 240, 128, 32, 144, 232, 72, 40, 24, 184, 0, 104, 216, 232,
         232, 176, 64, 168, 104, 8, 152, 56, 224, 168, 144, 96, 112, 56, 192,
         232, 136, 80, 152, 184, 176, 16, 168, 24, 88]
    total+=5
    print('nearestBusStop...Passed...5 pts')

def testCirclesIntersect():
    global total
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3,3,3,3,-3,3) == True)
    assert(circlesIntersect(3,3,3,3,-3,2.99) == False)
    groups=[[93, 39, 52, 41, 14, 20], [32, 89, 33, 97, 71, 37],
            [89, 10, 58, 13, 92, 15], [70, 90, 95, 89, 59, 51],
            [11, 40, 43, 9, 57, 80], [9, 54, 44, 14, 38, 38],
            [41, 84, 95, 82, 81, 72], [84, 26, 8, 79, 81, 94],
            [49, 36, 4, 48, 15, 39], [60, 28, 77, 35, 61, 78],
            [91, 83, 90, 90, 77, 49], [67, 14, 11, 33, 16, 6],
            [29, 11, 32, 6, 79, 14], [17, 90, 44, 20, 34, 5],
            [25, 5, 81, 99, 45, 100], [40, 8, 57, 41, 15, 74],
            [49, 98, 55, 2, 52, 1], [93, 42, 51, 34, 71, 69],
            [30, 72, 74, 55, 46, 29], [62, 20, 68, 71, 18, 65],
            [15, 23, 78, 26, 85, 99], [78, 27, 40, 4, 1, 93],
            [64, 79, 84, 10, 56, 39], [56, 38, 14, 49, 39, 71],
            [95, 17, 40, 31, 48, 86], [86, 24, 59, 58, 44, 44],
            [39, 88, 44, 79, 88, 27], [59, 91, 3, 91, 84, 90],
            [37, 95, 61, 22, 13, 83], [83, 39, 43, 69, 51, 30],
            [6, 26, 45, 24, 80, 48], [52, 53, 19, 21, 44, 10],
            [7, 78, 31, 93, 66, 38], [1, 63, 96, 37, 37, 95],
            [21, 18, 23, 56, 42, 47], [32, 3, 71, 2, 1, 18],
            [56, 4, 74, 40, 47, 39], [95, 70, 5, 69, 26, 15],
            [94, 16, 44, 69, 72, 87], [74, 67, 25, 99, 92, 11],
            [78, 26, 57, 56, 8, 70], [28, 61, 2, 71, 81, 36],
            [28, 78, 65, 93, 8, 58], [82, 24, 64, 14, 26, 5],
            [76, 51, 99, 44, 12, 7], [47, 2, 82, 26, 33, 33],
            [49, 92, 22, 52, 56, 31], [21, 41, 92, 17, 50, 56],
            [7, 81, 79, 54, 54, 8], [24, 40, 45, 24, 5, 20]]
    ints=[True, True, False, True, True, True, True, True, True, True, True,
          False, False, False, True, True, False, True, True, True, True, True,
          True, True, True, True, True, True, True, True, True, False, False,
          True, True, True, True, False, True, True, True, False, True, True,
          True, True, True, True, True, True]
    assert ints==[circlesIntersect(i[0],i[1],i[2],i[3],i[4],i[5]) for i in groups]
    total+=8
    print('circlesIntersect...Passed...8 pts')

def testNearestOdd():
    global total
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    assert(nearestOdd(-98765.4321)==-98765)
    nums=[368.5653, -477.005, 59.93, 362.198, -68.0, -247.0, -161.53, -724.33,
          45.649, -631.329, -281.5, 323.1, -898.0, -424.1, 495.0, -27.93, 357.0,
          -352.415, -316.8999, 553.0, 448.269, 786.9105, -14.3, 712.01, 712.0,
          -911.8945, -998.2, -647.2, -865.32, 716.166, 427.181, 613.7, -637.919,
          -919.0, -622.6, -869.3774, -122.5, -654.35, -285.86, 541.86, 40.0,
          69.0, -818.0, 590.0, 466.2381, 140.9584, -133.12, 340.7, -995.0,
          -20.203, -87.908, -674.7, -339.75, 495.095, 231.16, -915.079, -930.412,
          -161.0, 765.16, 855.82, -165.6, -359.0, -825.9794, -538.38, 84.0,
          447.9252, -738.622, 190.0866, -566.129, -293.0, 579.1562, -471.9,
          -642.6, 563.52, -352.4, 867.626, 818.93, -699.5, -935.0, 712.6, 675.17,
          -821.76, -414.0, -233.645, 413.0, 271.6, 310.0, -460.6, -375.4,
          -280.9744, 200.8164, -327.9, -262.5, -514.4393, 687.7308, 685.4,
          360.2782, 607.83, -351.4091, -658.721]
    assert [nearestOdd(item) for item in nums]== \
           [369, -477, 59, 363, -69, -247, -161, -725, 45, -631, -281, 323,
            -899, -425, 495, -27, 357, -353, -317, 553, 449, 787, -15, 713,
            711, -911, -999, -647, -865, 717, 427, 613, -637, -919, -623,
            -869, -123, -655, -285, 541, 39, 69, -819, 589, 467, 141, -133,
            341, -995, -21, -87, -675, -339, 495, 231, -915, -931, -161, 765,
            855, -165, -359, -825, -539, 83, 447, -739, 191, -567, -293, 579,
            -471, -643, 563, -353, 867, 819, -699, -935, 713, 675, -821, -415,
            -233, 413, 271, 309, -461, -375, -281, 201, -327, -263, -515, 687,
            685, 361, 607, -351, -659] 
    total+=8
    print('nearestOdd...Passed...8 pts')

def testEggCartons():
    global total
    assert eggCartons(0) == 0
    assert eggCartons(1) == 1
    assert eggCartons(2)==1
    assert eggCartons(12) == 1
    assert eggCartons(13) == 2
    assert eggCartons(24) == 2
    assert eggCartons(25) == 3
    assert eggCartons(28) == 3
    assert eggCartons(36) == 3
    assert eggCartons(2099) == 175
    assert eggCartons(2100) == 175
    assert eggCartons(2101) == 176
    x=[11, 55, 99, 143, 186, 230, 274, 318, 361, 405, 449, 493, 537, 580, 624,
     668, 712, 755, 799, 843, 887, 931, 974, 1018, 1062, 1106, 1149, 1193,
     1237, 1281, 1325, 1368, 1412, 1456, 1500, 1543, 1587, 1631, 1675, 1719,
     1762, 1806, 1850, 1894, 1937, 1981, 2025, 2069, 2113, 2156]
    z=[1, 5, 9, 12, 16, 20, 23, 27, 31, 34, 38, 42, 45, 49, 52, 56, 60, 63, 67,
       71, 74, 78, 82, 85, 89, 93, 96, 100, 104, 107, 111, 114, 118, 122, 125,
       129, 133, 136, 140, 144, 147, 151, 155, 158, 162, 166, 169, 173, 177,
       180]
    assert z==[eggCartons(y) for y in x]
    total+=5
    print('eggCartons...Passed...5 pts')

def testPascalsTriangleValue():
    global total
    assert pascalsTriangleValue(1234,0)==1
    assert pascalsTriangleValue(1234,1)==1234
    assert pascalsTriangleValue(1234,2)==760761
    assert [pascalsTriangleValue(50,i) for i in range(51)]== \
        [1, 50, 1225, 19600, 230300, 2118760, 15890700, 99884400,
        536878650, 2505433700, 10272278170, 37353738800, 121399651100,
        354860518600, 937845656300, 2250829575120, 4923689695575,
        9847379391150, 18053528883775, 30405943383200, 47129212243960,
        67327446062800, 88749815264600, 108043253365600,
        121548660036300, 126410606437752, 121548660036300,
        108043253365600, 88749815264600, 67327446062800,
        47129212243960, 30405943383200, 18053528883775,
        9847379391150, 4923689695575, 2250829575120,
        937845656300, 354860518600, 121399651100, 37353738800,
        10272278170, 2505433700, 536878650, 99884400, 15890700,
        2118760, 230300, 19600, 1225, 50, 1]
    total+=5
    print('pascalsTriangleValue...Passed...5 pts')

def testIsPerfectCube():
    global total
    assert isPerfectCube(27)==True
    assert isPerfectCube(-27)==True
    assert isPerfectCube(27.1)==False
    assert isPerfectCube(0)==True
    assert isPerfectCube(-1)==True
    assert isPerfectCube(12)==False
    assert isPerfectCube(-1234**3)
    assert isPerfectCube(-1234+.01**3)==False
    z=[-124998, -117648, -110593, -103822, -97335, -91126, -85184, -79508, -74086, -68920,
       -64000, -59317, -54874, -50651, -46656, -42877, -39305, -35935, -32768, -29792,
       -27002, -24389, -21950, -19685, -17578, -15626, -13824, -12166, -10646, -9260,
       -8001, -6857, -5832, -4915, -4098, -3373, -2743, -2195, -1727, -1332, -998, -727,
       -511, -344, -218, -123, -64, -26, -10, 1, -1, 1, 9, 29, 66, 126, 217, 342, 510,
       728, 999, 1329, 1730, 2196, 2746, 3373, 4094, 4915, 5831, 6858, 8002, 9260, 10650,
       12166, 13824, 15627, 17574, 19681, 21953, 24388, 27002, 29792, 32768, 35936, 39304,
       42874, 46654, 50654, 54871, 59321, 64001, 68922, 74089, 79505, 85186, 91124, 97336,
       103822, 110592, 117649]
    assert [isPerfectCube(item) for item in z]== \
        [False, False, False, False, False, False, True, False, False, False, True,
         False, False, False, True, False, False, False, True, False, False, True, False,
         False, False, False, True, False, False, False, False, False, True, False, False,
         False, False, False, False, False, False, False, False, False, False, False, True,
         False, False, True, True, True, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, True, False, False, False, False, False, False, False, True,
         False, True, False, False, False, False, False, False, False, False, False, False,
         False, True, False, True, True]
    total+=5
    print('isPerfectCube...Passed...5 pts')

def testIsEvenPositiveInt():
    global total
    assert isEvenPositiveInt(2)==True
    assert isEvenPositiveInt(23467812)==True
    assert isEvenPositiveInt(-2)==False
    assert isEvenPositiveInt(0)==False
    assert isEvenPositiveInt(2.1)==False
    assert isEvenPositiveInt(-2.2)==False
    assert isEvenPositiveInt(3)==False
    assert isEvenPositiveInt('yikes')==False
    assert [isEvenPositiveInt(i*1.4) for i in range(-5,50)]== \
        [False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, True, False, False, False, False, False, False,
         False, False, False, True, False, False, False, False, False, False, False,
         False, False, True, False, False, False, False, False, False, False, False,
         False, True, False, False, False, False, False, False, False, False, False]
    
    total+=5
    print('isEvenPositiveInt...Passed...5 pts')

def testCelsiusToFahrenheit():
    global total
    assert celsiusToFahrenheit(100)==212
    assert celsiusToFahrenheit(0)==32
    assert celsiusToFahrenheit(-40)==-40
    assert celsiusToFahrenheit(90)==194.0
    assert [round(celsiusToFahrenheit(i),1) for i in range(-10,110)]== \
        [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2, 32.0, 33.8, 35.6,
         37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0, 51.8, 53.6, 55.4, 57.2, 59.0,
         60.8, 62.6, 64.4, 66.2, 68.0, 69.8, 71.6, 73.4, 75.2, 77.0, 78.8, 80.6, 82.4,
         84.2, 86.0, 87.8, 89.6, 91.4, 93.2, 95.0, 96.8, 98.6, 100.4, 102.2, 104.0, 105.8,
         107.6, 109.4, 111.2, 113.0, 114.8, 116.6, 118.4, 120.2, 122.0, 123.8, 125.6,
         127.4, 129.2, 131.0, 132.8, 134.6, 136.4, 138.2, 140.0, 141.8, 143.6, 145.4,
         147.2, 149.0, 150.8, 152.6, 154.4, 156.2, 158.0, 159.8, 161.6, 163.4, 165.2,
         167.0, 168.8, 170.6, 172.4, 174.2, 176.0, 177.8, 179.6, 181.4, 183.2, 185.0,
         186.8, 188.6, 190.4, 192.2, 194.0, 195.8, 197.6, 199.4, 201.2, 203.0, 204.8,
         206.6, 208.4, 210.2, 212.0, 213.8, 215.6, 217.4, 219.2, 221.0, 222.8, 224.6,
         226.4, 228.2]
    total+=5
    print('celsiusToFahrenheit...Passed...5 pts')

def testFahrenheitToCelsius():
    global total
    assert fahrenheitToCelsius(212)==100
    assert fahrenheitToCelsius(32)==0
    assert fahrenheitToCelsius(-40)==-40
    assert almostEqual(fahrenheitToCelsius(184),84.44444444444444)
    assert [round(fahrenheitToCelsius(i),2) for i in range(-10,220,3)]== \
        [-23.33, -21.67, -20.0, -18.33, -16.67, -15.0, -13.33, -11.67, -10.0, -8.33,
         -6.67, -5.0, -3.33, -1.67, 0.0, 1.67, 3.33, 5.0, 6.67, 8.33, 10.0, 11.67,
         13.33, 15.0, 16.67, 18.33, 20.0, 21.67, 23.33, 25.0, 26.67, 28.33, 30.0,
         31.67, 33.33, 35.0, 36.67, 38.33, 40.0, 41.67, 43.33, 45.0, 46.67, 48.33,
         50.0, 51.67, 53.33, 55.0, 56.67, 58.33, 60.0, 61.67, 63.33, 65.0, 66.67,
         68.33, 70.0, 71.67, 73.33, 75.0, 76.67, 78.33, 80.0, 81.67, 83.33, 85.0,
         86.67, 88.33, 90.0, 91.67, 93.33, 95.0, 96.67, 98.33, 100.0, 101.67, 103.33]
    total+=5
    print('fahrenheitToCelsius...Passed...5 pts')

def testAreCollinear():
    global total
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 5, 2, math.pi)==True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    z=[9, 5, 5, 7, 1, 5, 7, 2, 7, 6, 9, 6, 3, 8, 8, 8, 7, 2, 7, 6, 2, 6, 8, 1,
       8, 9, 7, 5, 9, 1, 9, 4, 3, 4, 9, 2, 9, 8, 5, 3, 5, 6, 3, 3, 7, 8, 9, 5,
       3, 3, 3, 3, 6, 3, 7, 4, 2, 4, 9, 8, 3, 2, 5, 2, 6, 9, 2, 7, 7, 7, 1, 1,
       2, 5, 1, 9, 8, 8, 7, 7, 4, 5, 7, 7, 4, 7, 9, 4, 6, 7, 8, 9, 7, 8, 3, 1,
       6, 1, 9, 7, 6, 1, 7, 4, 1, 9, 1, 1, 7, 5, 9, 8, 1, 3, 8, 7, 4, 2, 8, 1]
    assert [areCollinear(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5]) \
            for i in range(len(z)-6)]== \
        [False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False,
         False, False, True, False, True, True, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False, False, False, False, False, False, False, False,
         False, True, True, False, False, False, False, False, False, False, False,
         True, False, False, False, False, False, False, False, True, False, False,
         False, False, False, False, False, False, False, False, False, False, False,
         False, False, False, False]
    total+=10
    print('areCollinear...Passed...7 pts')
    
def testNumberOfPoolBalls():
    global total
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3) 
    assert(numberOfPoolBalls(3) == 6) 
    assert(numberOfPoolBalls(10) == 55) 
    triangulars=[round(n*(n+1)/2) for n in range(100)]
    assert triangulars==[numberOfPoolBalls(i) for i in range(100)]
    total+=7
    print('numberOfPoolBalls...Passed...7 pts')
    
def testNumberOfPoolBallRows():
    global total
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    poolBalls=[0, 2, 1, 7, 10, 14, 20, 28, 36, 46, 55, 64, 76, 91, 106, 121, 135, 154,
               169, 189, 211, 229, 252, 276, 298, 326, 351, 379, 407, 433, 464, 497,
               526, 559, 596, 629, 667, 704, 742, 780, 819, 860, 901, 946, 991, 1035,
               1081, 1127, 1177, 1225, 1275, 1325, 1379, 1432, 1486, 1540, 1595, 1654,
               1712, 1769, 1831, 1890, 1952, 2017, 2080, 2144, 2209, 2277, 2345, 2416,
               2483, 2556, 2629, 2702, 2774, 2851, 2926, 3004, 3079, 3161, 3239, 3321,
               3404, 3484, 3570, 3655, 3740, 3828, 3916, 4005, 4093, 4184, 4276, 4372,
               4466, 4561, 4656, 4754, 4850, 4951]
    assert [round(numberOfPoolBallRows(item)) for item in poolBalls]== \
          [0, 2, 1, 4, 4, 5, 6, 7, 8, 10, 10, 11, 12, 13, 15, 16, 16, 18, 18, 19, 21, 21,
           22, 23, 24, 26, 26, 28, 29, 29, 30, 32, 32, 33, 35, 35, 37, 38, 39, 39, 40, 41,
           42, 43, 45, 45, 46, 47, 49, 49, 50, 51, 53, 54, 55, 55, 56, 58, 59, 59, 61, 61,
           62, 64, 64, 65, 66, 67, 68, 70, 70, 71, 73, 74, 74, 76, 76, 78, 78, 80, 80, 81,
           83, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 96, 98, 98, 100]
    total+=7
    print('numberOfPooBallRows...Passed...7 pts')

def testSphereVolumeFromSurfaceArea():
    global total
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904.7786778830696) == True) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.09734223538379) == True) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  905) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113) == False) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.1) == False)
    assert [round(sphereVolumeFromSurfaceArea(i),3) for i in range(50,1000,50)]== \
        [33.245, 94.032, 172.747, 265.962, 371.693, 488.603, 615.71, 752.253,
         897.62, 1051.305, 1212.88, 1381.977, 1558.274, 1741.49, 1931.371, 2127.692,
         2330.248, 2538.853, 2753.336]
    total+=5
    print('sphereVolumeFromSurfaceArea...Passed...5 pts')
    
def testSetKthDigit():
    global total
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    assert(setKthDigit(12345678,5,9)==12945678)
    from math import exp
    num=round(exp(1)*10**15)
    digits=[i%10 for i in range(5,123,8)]
    assert [setKthDigit(num,i,digits[i]) for i in range(len(digits))]== \
        [2718281828459045, 2718281828459035, 2718281828459145, 2718281828459045,
         2718281828479045, 2718281828559045, 2718281823459045, 2718281818459045,
         2718281928459045, 2718287828459045, 2718251828459045, 2718381828459045,
         2711281828459045, 2798281828459045, 2718281828459045]  
    total+=10
    print('setKthDigit...Passed...10 pts')

def testCosineZerosCount():
    global total
    assert(type(cosineZerosCount(0)) == int)
    assert(cosineZerosCount(0) == 0)
    assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
    assert(cosineZerosCount(10*math.pi/2 - 0.0001) == 5)
    assert(cosineZerosCount(101*math.pi/2 + 0.0001) == 51)
    assert(cosineZerosCount(101*math.pi/2 - 0.0001) == 50)
    x=[round(math.pi/2*i+(-1)**i*.02,4) for i in range(7,200,5)]
    assert [cosineZerosCount(item) for item in x]== \
        [3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31, 33, 36, 38, 41, 43, 46, 48, 51, 53, 56,
         58, 61, 63, 66, 68, 71, 73, 76, 78, 81, 83, 86, 88, 91, 93, 96, 98]
    total+=10
    print('cosineZerosCount...Passed...10 pts')

def testRiverCruiseUpstreamTime():
    global total
    # example from the source notes:
    totalTime = 3 
    totalDistance = 30 
    riverCurrent = 2 
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,totalDistance,riverCurrent),
                       1.7888736053508778))
    assert(almostEqual(riverCruiseUpstreamTime(3,30,0),1.5))
    assert(almostEqual(riverCruiseUpstreamTime(4,56,2),2.2801098892805185))
    total+=10
    print('riverCruiseUpstream...Passed...10 pts')

def testQuadrilateralArea():
    global total
    assert(almostEqual(quadrilateralArea(0, 0, 0, 3, 5, 3, 5, 0),15))
    assert(almostEqual(quadrilateralArea(15, 17, 22, 17, 21, 20, 18, 20), 15))
    assert(almostEqual(quadrilateralArea(9, 6, 15, 6, 18, 9, 12, 9), 18))
    assert(almostEqual(quadrilateralArea(-5, 1, 2, -7, 10, 8, -2, 5), 104))
    assert(almostEqual(quadrilateralArea(0,0,4,3,-2,11,-6,8), 50))
    z=[9, -4, -40, -29, -40, -13, -10, 39, 22, 18, 1, -27, -32, -11, 0, 15, -31, 27, 5, 39, 33,
       20, 18, -17, 25, 8, 7, -20, -17, -14, -26, 18, 16, -7, 3, -14, -38, 8, -38, 25, -28, -21,
       -19, 26, -6, 32, 4, 22, 28, -11, 33, -16, -26, 12, 2, 6, -34, -30, -5, -7, 22, 3, 9, -29,
       37, 9, -20, -39, -35, -2, -38, 15, -33, 0, 3, 27, 19, 30, 25, 5, 11, -18, 16, 32, -10,
       -20, -19, 0, 4, 39]
    assert [round(quadrilateralArea(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5],z[i+6],z[i+7]),2)
            for i in range(len(z)-8)]== \
        [1531.0, 1299.0, 1643.0, 587.0, 2216.5, 474.0, 1941.5, 750.0, 1148.5, 6.5, 40.0, 86.0,
         83.0, 1156.0, 785.5, 380.0, 1746.5, 392.0, 302.0, 260.0, 54.0, 235.5, 58.0, 412.5,
         1161.0, 264.0, 742.5, 435.5, 629.5, 275.0, 646.5, 1061.0, 745.5, 874.5, 399.5, 515.5,
         280.5, 328.5, 492.5, 571.5, 653.5, 947.0, 426.5, 673.0, 22.5, 1712.0, 692.5, 1210.0,
         237.5, 249.0, 739.0, 245.0, 95.0, 1221.5, 248.5, 1015.0, 847.0, 401.5, 207.0, 274.0,
         12.0, 361.0, 200.5, 306.0, 2043.0, 475.0, 72.0, 1105.0, 29.0, 194.0, 303.0, 648.0,
         902.0, 122.0, 616.0, 93.0, 324.0, 625.5, 292.5, 493.5, 301.0, 574.0]
    total+=6
    print('quadrilateralArea...Passed...6 points')



def testRectanglesOverlap():
    global total
    assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6)==True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6)==False)
    assert (rectanglesOverlap(0,0,20,20,5,5,5,5)==True)
    z=[9, 5, 5, 7, 1, 5, 7, 2, 7, 6, 9, 6, 3, 8, 8, 8, 7, 2, 7, 6, 2, 6, 8, 1,
       8, 9, 7, 5, 9, 1, 9, 4, 3, 4, 9, 2, 9, 8, 5, 3, 5, 6, 3, 3, 7, 8, 9, 5,
       3, 3, 3, 3, 6, 3, 7, 4, 2, 4, 9, 8, 3, 2, 5, 2, 6, 9, 2, 7, 7, 7, 1, 1,
       2, 5, 1, 9, 8, 8, 7, 7, 4, 5, 7, 7, 4, 7, 9, 4, 6, 7, 8, 9, 7, 8, 3, 1,
       6, 1, 9, 7, 6, 1, 7, 4, 1, 9, 1, 1, 7, 5, 9, 8, 1, 3, 8, 7, 4, 2, 8, 1]
    assert [rectanglesOverlap(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5],z[i+6],z[i+7]) \
            for i in range(len(z)-8)]== \
        [False, False, False, True, True, True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, False, False, True, True, False, False, True, True,
         True, True, True, True, False, False, True, False, False, True, True, True, True, True,
         True, False, False, False, True, True, True, True, True, True, True, True, True, True,
         True, True, True, True, False, False, True, True, False, False, False, False, False,
         True, False, False, False, True, True, True, True, True, True, True, True, True, True,
         True, True, True, True, True, True, True, False, False, True, True, False, False, True,
         False, False, False, False, False, True, False, False, False, False, False, True, True,
         True, True]
    total+=10
    print('rectanglesOverlap...Passed...10 pts')

def testLineIntersection():
    global total
    assert(lineIntersection(2.5, 3, 2.5, 11) == False)
    assert(lineIntersection(25, 3, 25, 11) == False)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    assert(almostEqual(lineIntersection(10,0,-4,15),1.0714285714285714))
    print('lineIntersection...Passed')

def testThreeLinesArea():
    global total
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    z=[9, 5, 5, 7, 1, 5, 7, 2, 7, 6, 9, 6, 3, 8, 8, 8, 7, 2, 7, 6, 2, 6, 8, 1,
       8, 9, 7, 5, 9, 1, 9, 4, 3, 4, 9, 2, 9, 8, 5, 3, 5, 6, 3, 3, 7, 8, 9, 5,
       3, 3, 3, 3, 6, 3, 7, 4, 2, 4, 9, 8, 3, 2, 5, 2, 6, 9, 2, 7, 7, 7, 1, 1,
       2, 5, 1, 9, 8, 8, 7, 7, 4, 5, 7, 7, 4, 7, 9, 4, 6, 7, 8, 9, 7, 8, 3, 1,
       6, 1, 9, 7, 6, 1, 7, 4, 1, 9, 1, 1, 7, 5, 9, 8, 1, 3, 8, 7, 4, 2, 8, 1]    
    assert [round(threeLinesArea(z[i],z[i+1],z[i+2],z[i+3],z[i+4],z[i+5]),3) \
            for i in range(len(z)-6)]== \
        [1.0, 0, 6.0, 5.4, 0, 1.5, 0, 0, 0.167, 0, 1.667, 0, 22.5, 0, 0, 9.375,
         0, 0, 10.417, 0, 0, 0.104, 0, 0.562, 36.0, 0.25, 0, 24.0, 0, 0, 0, 0,
         0, 0.667, 0, 6.667, 0, 1.667, 0, 0, 0.125, 11.267, 5.042, 9.6, 5.042,
         2.4, 0, 0, 0, 0, 0.375, 0, 0.625, 0, 2.857, 0, 3.857, 8.167, 1.5, 0,
         16.333, 0, 28.167, 5.207, 2.5, 0, 15.0, 0, 5.4, 0.042, 0, 4.0, 8.679,
         0.375, 0.762, 1.0, 0.042, 6.75, 0, 0, 0, 0, 1.35, 0, 0.6, 0, 12.0,
         0.817, 0.0, 20.25, 0.225, 8.58, 18.375, 0, 3.0, 0, 0, 0, 0.75, 10.083,
         8.817, 3.75, 0, 3.75, 0, 6.25, 0.521, 8.595, 1.021, 6.017, 0.08, 1.6,
         2.149, 0.4]
    total+=15
    print('threeLinesArea...Passed...15 pts')

def testFindCubicRoots():
    global total
    assert findCubicRoots(1,9,26,24)==(-4,-3,-2)
    assert findCubicRoots(2,-12,-158,-312)==(-4,-3,13)
    assert findCubicRoots(5,-95,50,2040)==(-4,6,17)
    x=[1, 8, 19, 12, 1, 2, -23, -60, 1, 2, -23, -60, 1, -2, -19, 20, 1, 8, 11, -20, 1, 1,
       -17, 15, 1, -1, -21, 45, 1, -5, 3, 9, 1, -4, 1, 6, 1, 4, -7, -10, 1, -1, -22, 40,
       1, 6, -15, -100, 1, 1, -20, 0, 1, 8, 15, 0, 1, 8, 15, 0, 1, 3, -25, -75, 1, 5, -25,
       -125, 1, -1, -25, 25, 1, 7, 7, -15, 1, 2, -3, 0]
    assert [findCubicRoots(x[i],x[i+1],x[i+2],x[i+3]) for i in range(0,len(x),4)]== \
        [(-4, -3, -1), (-4, -3, 5), (-4, -3, 5), (-4, 1, 5), (-5, -4, 1), (-5, 1, 3),
         (-5, 3, 3), (-1, 3, 3), (-1, 2, 3), (-5, -1, 2), (-5, 2, 4), (-5, -5, 4),
         (-5, 0, 4), (-5, -3, 0), (-5, -3, 0), (-5, -3, 5), (-5, -5, 5), (-5, 1, 5),
         (-5, -3, 1), (-3, 0, 1)]
    total+=10
    print('findCubicRoots....passed...10 pts')
    
def testColorBlender():
    global total
    assert colorBlender(220020060, 189252201, 3, 1) ==212078095
    assert colorBlender(78001, 60008065, 40, 29)== 42028046
    assert colorBlender(255000204,254002203,8,2)==255000204
    assert colorBlender(255000204,254002203,8,3)==255001204
    colors=[colorBlender(255001204, 78201009, 100,i) for i in range(-5,110,3)]
    assert colors==['Error', 'Error', 253003202, 248009196, 243015190, 237021185,
                    232027179, 227033173, 222039167, 216045162, 211051156,
                    206056150, 201062144, 195068138, 190074133, 185080127,
                    180086121, 174092115, 169098109, 164104104, 159110098,
                    153116092, 148122086, 143128080, 138134075, 132140069,
                    127146063, 122151057, 117157051, 111163046, 106169040,
                    101175034, 96181028, 90187023, 85193017, 80199011,
                    'Error', 'Error', 'Error']
    total+=15
    print('colorBlender....passed...15 pts')

def testIsSpecialQuadrilateral():
    global total
    assert isSpecialQuadrilateral(5,5,2,-2,-1,-1,-2,2)=='Kite'
    assert isSpecialQuadrilateral(5,5,5,-6,-8,-6,-8,5)=='Rectangle'
    assert isSpecialQuadrilateral(3,7,3,1,10,4,10,10)=='Parallelogram'
    assert isSpecialQuadrilateral(-6,7,-3,3,0,7,-3,20)=='Kite'
    assert isSpecialQuadrilateral(-8,4,-5,2,-1,4,-10,10)=='Trapezoid'
    assert isSpecialQuadrilateral(-8,-4,-5,2,-1,4,-10,10)=='Not a Special Quadrilateral'
    assert isSpecialQuadrilateral(3,-2,-1,-10,-6,-12,-2,-4)=='Parallelogram'
    assert isSpecialQuadrilateral(-7,6,-2,18,10,13,5,1)=='Square'
    assert isSpecialQuadrilateral(1,5,4,1,12,7,9,11)=='Rectangle'
    assert isSpecialQuadrilateral(2,5,6,6,5,2,1,1)=='Rhombus'
    assert isSpecialQuadrilateral(2,2,-2,2,-2,-2,2,-2)=='Square'
    assert isSpecialQuadrilateral(-10,-3,11,17,51,-25,9,-65)=='Trapezoid'
    assert isSpecialQuadrilateral(-2,0,2,-1,3,3,-1,4)=='Square'
    assert isSpecialQuadrilateral(-3,-4,1,-5,3,3,-1,4)=='Rectangle'
    assert isSpecialQuadrilateral(-3,-4,0,-9,3,3,-1,4)=='Trapezoid'
    specials=[[-19, -42, -36, 9, -34, 15, 2, 21], [-31, 13, -9, 24, -20, -19, -40, -29],
              [19, -12, -36, -41, -1, 29, 25, 0], [-10, 5, -17, 23, -17, 25, -10, 16],
              [6, 19, 27, 2, 40, -47, -2, -13], [34, 12, -6, -12, 5, 32, 36, 20],
              [46, -39, 14, -41, 11, -32, 45, -36], [23, 16, -11, -24, -45, -2, 6, 27],
              [25, 49, 28, 50, 15, 32, -45, 12], [8, -30, -26, 10, -26, 23, 8, 29],
              [-26, 10, -26, 23, 8, 29, 8, -1], [-19, 43, 3, -11, 3, -17, -19, -39],
              [-38, -49, -26, -21, 0, 5, 41, 30], [31, 23, -3, -14, -19, -6, 21, 28],
              [-6, -13, -50, -9, -14, 41, -3, 40], [41, -15, -5, -25, -7, -25, 24, -15],
              [-15, -5, -25, -7, -25, 24, -15, 23], [-36, -29, -18, -28, -7, -28, 19, -29],
              [19, -4, -28, 18, -1, 32, 46, 10], [15, 25, 21, 18, -8, -12, -32, 16],
              [2, 3, -40, -21, -44, 14, -16, 30], [-21, 32, 41, -17, -44, -17, -50, 32],
              [-32, -14, 2, -31, -34, -16, -44, -11], [-16, -14, 35, -26, -33, -43, -20, -15],
              [19, -26, -14, 7, 34, -2, 40, -8], [11, 6, -6, -5, 30, 23, 38, 27],
              [-11, 5, -4, 25, -4, -41, -11, -36], [26, -50, 0, -42, 48, 30, 50, -14],
              [-15, 24, 18, 31, 39, -33, 6, -40], [16, -47, -46, -47, -5, -26, 47, -26],
              [8, 50, 12, -10, 8, -12, 4, -10], [-9, -36, -50, 5, -20, -1, 21, -42],
              [36, -3, 46, -23, 47, -38, 39, -48], [-1, -44, -48, -35, -2, -39, 22, -46],
              [14, -11, 14, -31, 6, -47, 6, 19], [-37, -10, -38, -3, -3, 3, 2, -32],
              [-44, -1, -8, 35, 2, -14, -3, -19], [-16, 46, -9, 39, -25, -21, -34, -12],
              [-50, 36, -8, 36, -13, -43, -19, -43], [36, -8, 36, -13, -43, -19, -43, -12],
              [44, -8, 4, -7, -37, 34, 30, 6], [46, 13, -23, -22, -38, -16, -29, 43],
              [36, 2, 38, -27, 32, -27, 2, 2], [-39, -15, 35, 28, 39, 28, -17, -15],
              [-15, 35, 28, 39, 28, -17, -15, -23], [34, 50, 39, 49, 9, -35, -1, -33],
              [-37, -20, 21, -13, 39, -41, -28, -34], [-40, -1, -48, -7, -2, 39, 2, 42],
              [-12, 16, 12, 26, 40, 12, 22, -1], [25, 35, 34, 30, 26, -28, -10, -8],
              [-30, 7, -15, -38, -38, -45, -48, -15], [-30, -16, 27, 36, 39, 18, -8, -49],
              [33, 39, 36, 14, 16, 19, 9, 45], [-33, 29, -35, 35, 34, -19, 41, -40],
              [-36, 35, -36, 40, 17, 49, 17, -40], [44, 19, 30, 5, -37, 43, -31, 49],
              [29, -24, 37, 3, 46, -6, 34, -29], [8, -21, 50, -31, 4, -31, -12, -21],
              [-39, 28, 15, 12, -41, 18, -45, 24], [5, -12, -7, 0, 1, -4, 29, -32],
              [41, 19, 38, -4, -27, -4, -2, 19], [17, -13, -14, -46, -24, -34, -33, 47],
              [-23, -4, 18, -39, 18, -45, -23, -34], [18, -36, -23, -37, -36, 15, 2, 28],
              [-4, -43, -42, -31, -41, -30, 10, -29], [22, 20, 20, -26, 13, -47, 9, -19],
              [46, -16, -9, -41, 5, 34, 27, 44], [29, 20, 29, -34, -4, -26, -4, -25],
              [-12, 45, -7, 12, -13, 12, -16, 45], [11, 40, 11, -32, 10, -27, 10, -21],
              [-11, 39, -50, 46, -32, 46, 9, 39], [-4, 24, 14, -3, 10, -48, 6, -42],
              [-4, 24, 16, 27, 20, 6, -20, 0], [27, -27, -37, -7, -50, 45, 14, 25],
              [-36, 46, 2, 33, 2, 24, -36, 31], [11, 4, -27, -42, -5, 24, 20, 31],
              [30, -3, -44, -21, 9, 32, 33, 0], [14, -40, -42, -8, 30, -8, 23, -40]]
    quads=['Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Parallelogram', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Parallelogram', 'Trapezoid',
           'Kite', 'Parallelogram', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Kite', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid', 'Parallelogram', 'Trapezoid',
           'Trapezoid', 'Trapezoid', 'Trapezoid']
    assert [isSpecialQuadrilateral(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
            for i in specials]==quads
    total+=20
    print('isSpecialQuadrilateral...Passed...20 pts')

#############################################################################
#############################################################################

def testAll():
    if isPerfectSquare(1)!=None:
        testisPerfectSquare()
        pass
    if isFactor(1,1)!=None:
        testIsFactor()
        pass
    if isMultiple(1,1)!=None:
        testIsMultiple()
        pass
    if kthDigit(1,1)!=None:
        testKthDigit()
        pass
    if distance(1,1,1,1)!=None:
        testDistance()
        pass
    if isLegalTriangle(1,1,1)!=None:
        testIsLegalTriangle()
        pass
    if isRightTriangle(1,1,1,1,1,1)!=None:
        testIsRightTriangle()
        pass
    if triangleAreaByCoordinates(1,1,1,1,1,1)!=None:
        testTriangleAreaByCoordinates()
        pass
    if nthFibonacci(0)!=None:
        testNthFibonacci()
        pass
    if fabricExcess(1)!=None:
        testFabricExcess()
        pass
    if nearestBusStop(1)!=None:
        testNearestBusStop()
        pass
    if circlesIntersect(1,1,1,1,1,1)!=None:
        testCirclesIntersect()
        pass
    if nearestOdd(1)!=None:
        testNearestOdd()
        pass
    if eggCartons(1)!=None:
        testEggCartons()
        pass
    if pascalsTriangleValue(1,1)!=None:
        testPascalsTriangleValue()
        pass
    if isPerfectCube(1)!=None:
        testIsPerfectCube()
        pass
    if isEvenPositiveInt(1)!=None:
        testIsEvenPositiveInt()
        pass
    if celsiusToFahrenheit(1)!=None:
        testCelsiusToFahrenheit()
        pass
    if fahrenheitToCelsius(1)!=None:
        testFahrenheitToCelsius()
        pass
    if areCollinear(1,1,1,1,1,1)!=None:
        testAreCollinear()
        pass
    if numberOfPoolBalls(1)!=None:
        testNumberOfPoolBalls()
        pass
    if numberOfPoolBallRows(1)!=None:
        testNumberOfPoolBallRows()
        pass
    if sphereVolumeFromSurfaceArea(1)!=None:
        testSphereVolumeFromSurfaceArea()
        pass
    if setKthDigit(1,1,1)!=None:
        testSetKthDigit()
        pass
    if cosineZerosCount(1)!=None:
        testCosineZerosCount()
        pass
    if riverCruiseUpstreamTime(1,1,1)!=None:
        testRiverCruiseUpstreamTime()
        pass
    if rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)!=None:
        testRectanglesOverlap()
        pass
    if quadrilateralArea(1,2,3,4,5,6,7,8)!=None:
        testQuadrilateralArea()
        pass
    if threeLinesArea(1,1,1,1,1,1)!=None:
        testThreeLinesArea()
        pass
    if findCubicRoots(1,0,0,-1)!=None:
        testFindCubicRoots()
        pass
    if colorBlender(123123123,245245245,3,1)!=None:
        testColorBlender()
        pass
    if isSpecialQuadrilateral(1,2,3,4,5,6,7,8)!=None:
        testIsSpecialQuadrilateral()
        pass

total=0
testAll()
print()
print('Total Score...',total)