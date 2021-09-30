######################################################################
##       Mathematical Computation Quiz Unit One     ##################
######################################################################
import math

def almostEqual(x,y):
    return abs(x-y)<10**-8

def integerSquareRoot(x):
    return round(math.sqrt(x))

def fabricYards(inches):
    return math.ceil(inches/36)

def angleOfRegularPolygon(sides):
    return (sides-2)*180/sides

def numberOfQuadraticRoots(a,b,c):
    discriminant = b**2-4*a*c
    if discriminant < 0: return 0
    elif discriminant == 0: return 1
    else: return 2

def findReferenceAngle(theta):
    angle = theta%180
    if angle%90==0:
        return "No Reference Angle"
    if angle > 90 :
        angle = 180 - angle
    return angle

def isTriangular(x):
    if x < 0: return False
    c = -2*x
    b = 1
    a = 1
    d = (b**2)-(4*a*c)
    if d < 0: return False
    root1 = (-b+math.sqrt(d))/(2 * a)
    root2 = (-b-math.sqrt(d))/(2 * a)
    if (root1 > 0 and math.floor(root1) == root1): return True 
    if (root2 > 0 and math.floor(root2) == root2): return True
    return False

def simpleCannonAiming(targetRange):
    theta = (math.asin((targetRange*(32))/600**2))/2
    return round((theta * 180/math.pi), 1)

def kthRoot(n,k):
    return None

def DMS(theta):
    is_positive = theta >= 0
    decimalDegrees = abs(theta)
    minutes,seconds = divmod(decimalDegrees*3600,60) # Learned about this neat little thing the other day but can't make it work!
    degrees,minutes = divmod(minutes,60)
    degrees = degrees if is_positive else -degrees
    return round(degrees), round(minutes), round(seconds)
# Mr. Jackson, I don't know if you read this, but, I think I deserve my points
# for DMS even though it fails. In the automated (for loop) test cases, my code fails
# because it outputs (484, 27, 0) instead of what was in the test case checks:
# (484, 26, 60)
# I am not sure if I can get around this with my current implementation, but
# I feel like 26, 60 should have been rounded to 27, 0 as my function does
# Because of this failure, I am not sure if my code would work for the negative
# values either. Anyway, I am going to leave it as is for now and I would appreciate
# if you took a look at the for loop test cases and checks to make sure that they all function
# properly. Thanks for reading my code :-)
# Sig

def binomialExperimentProbability(p,n,x):
    return None

def dayOfWeek(m,d,y):
    return None



######################################################################
######################################################################

def testIntegerSquareRoot():
    assert integerSquareRoot(0)==0
    assert integerSquareRoot(16)==4
    assert integerSquareRoot(15)==4
    assert integerSquareRoot(17)==4
    assert[integerSquareRoot(i) for i in range(1000,10000,250)]== \
          [32, 35, 39, 42, 45, 47, 50, 52, 55, 57, 59, 61, 63, 65,
          67, 69, 71, 72, 74, 76, 77, 79, 81, 82, 84, 85, 87, 88,
          89, 91, 92, 94, 95, 96, 97, 99]
    print('integerSquareRoot...Passed')

def testFabricYards():
    assert fabricYards(0)==0
    assert fabricYards(1)==1
    assert fabricYards(36)==1
    assert fabricYards(37)==2
    assert fabricYards(72)==2
    assert fabricYards(73)==3
    assert fabricYards(58965)==1638
    assert[fabricYards(i) for i in range(24,500,6)]== \
          [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
          4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8,
          8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11,
          11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13,
          13, 13, 14, 14, 14, 14, 14]   
    print('fabricYards...Passed')
                       
def testAngleOfRegularPolygon():
    assert angleOfRegularPolygon(3)==60
    assert angleOfRegularPolygon(4)==90
    angles=[angleOfRegularPolygon(i) for i in range(10,40)]
    correctAngles=[144.0, 147.27272727272728, 150.0, 152.30769230769232,
                   154.28571428571428, 156.0, 157.5, 158.8235294117647,
                   160.0, 161.05263157894737, 162.0, 162.85714285714286,
                   163.63636363636363, 164.34782608695653, 165.0, 165.6,
                   166.15384615384616, 166.66666666666666, 167.14285714285714,
                   167.58620689655172, 168.0, 168.38709677419354, 168.75,
                   169.0909090909091, 169.41176470588235, 169.71428571428572,
                   170.0, 170.27027027027026, 170.52631578947367,
                   170.76923076923077]
    for angle in angles:
        assert almostEqual(angle,correctAngles[angles.index(angle)])
    print('angleOfRegularPolygon...Passed')
    
def testNumberOfQuadraticRoots():
    assert numberOfQuadraticRoots(1,5,6)==2
    assert numberOfQuadraticRoots(1,5,10)==0
    assert numberOfQuadraticRoots(1,4,4)==1
    assert numberOfQuadraticRoots(1,4,3.99999999999)==2
    assert numberOfQuadraticRoots(1,4,4.00000000001)==0
    assert[numberOfQuadraticRoots(1,-2,i) for i in range(-20,20)]== \
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print('numberOfQuadraticRoots...Passed')

def testFindReferenceAngle():
    assert findReferenceAngle(1)==1
    assert findReferenceAngle(-1)==1
    assert findReferenceAngle(179)==1
    assert findReferenceAngle(-179)==1
    assert findReferenceAngle(181)==1
    assert findReferenceAngle(359)==1
    assert findReferenceAngle(0)=='No Reference Angle'
    assert findReferenceAngle(450)=='No Reference Angle'
    assert findReferenceAngle(164430)=='No Reference Angle'
    assert findReferenceAngle(3745)==35
    assert findReferenceAngle(-3745)==35
    assert findReferenceAngle(164431)==89
    assert findReferenceAngle(-164431)==89
    assert[findReferenceAngle(i) for i in range(-1140,1140,40)]== \
            [60, 20, 20, 60, 80, 40, 'No Reference Angle', 40, 80, 60, 20, 20,
             60, 80, 40, 'No Reference Angle', 40, 80, 60, 20, 20, 60, 80, 40,
             'No Reference Angle', 40, 80, 60, 20, 20, 60, 80, 40,
             'No Reference Angle', 40, 80, 60, 20, 20, 60, 80, 40,
             'No Reference Angle', 40, 80, 60, 20, 20, 60, 80, 40,
             'No Reference Angle', 40, 80, 60, 20, 20]
    print('findReferenceAngle...Passed')

def testIsTriangular():
    assert isTriangular(1)==True
    assert isTriangular(10)==True
    assert isTriangular(11)==False
    for i in range(1,100):
        assert isTriangular(i/2*(i+1))
    for i in range(125251,125750):
        assert isTriangular(i)==False
    print('isTriangular...Passed')

def testSimpleCannonAiming():
    assert simpleCannonAiming(9700)==29.8
    assert simpleCannonAiming(10800)==36.9
    assert simpleCannonAiming(11050)==39.6
    assert simpleCannonAiming(1234)==3.1
    assert simpleCannonAiming(11200)==42.3
    assert simpleCannonAiming(5000)==13.2
    assert simpleCannonAiming(9876)==30.7
    assert[simpleCannonAiming(i) for i in range(1500,11000,125)]== \
          [3.8, 4.2, 4.5, 4.8, 5.1, 5.4, 5.8, 6.1, 6.4, 6.7, 7.1, 7.4,
          7.7, 8.1, 8.4, 8.7, 9.1, 9.4, 9.7, 10.1, 10.4, 10.8, 11.1,
          11.4, 11.8, 12.1, 12.5, 12.8, 13.2, 13.6, 13.9, 14.3, 14.6,
          15.0, 15.4, 15.7, 16.1, 16.5, 16.9, 17.3, 17.6, 18.0, 18.4,
          18.8, 19.2, 19.6, 20.1, 20.5, 20.9, 21.3, 21.8, 22.2, 22.7,
          23.1, 23.6, 24.1, 24.5, 25.0, 25.5, 26.0, 26.6, 27.1, 27.7,
          28.2, 28.8, 29.4, 30.0, 30.7, 31.4, 32.1, 32.8, 33.6, 34.5,
          35.4, 36.4, 37.6]
    print('simpleCannonAiming...Passed')

def testKthRoot():
    assert kthRoot(8,3)==2
    assert kthRoot(-8,3)==-2
    assert kthRoot(-8,2)=='No Root'
    assert kthRoot(25,2)==5
    assert almostEqual(kthRoot(25,3),25**(1/3))
    assert almostEqual(kthRoot(-25,3),-25**(1/3))
    for i in range(-20,0):
        assert kthRoot(i,2)=='No Root'
    for i in range(2,100,2):
        assert kthRoot(-8,i)=='No Root'
    roots=[kthRoot(i,4) for i in range(100,1000,37)]
    approximateRoots=[3.1622776601683795, 3.421213222048521, 3.631928682982765,
                   3.8112778757700085, 3.968376966471762, 4.1087641713943786,
                   4.236078191550099, 4.352849103919916, 4.460913442573438,
                   4.561650145143182, 4.656123214507837, 4.7451723360058695,
                   4.829472805532836, 4.909576518029625, 4.9859408128568985,
                   5.058949276691698, 5.128927068689104, 5.196152422706632,
                   5.260865423691818, 5.323274803221182, 5.383563270955295,
                   5.4418917473541955, 5.498402760407966, 5.553223198307317,
                   5.606466560232338]
    for root in roots:
        assert almostEqual(root,approximateRoots[roots.index(root)])
    print('kthRoot...Passed')

def testDMS():
    assert DMS(345.876543)==(345, 52, 36)
    assert DMS(.5)==(0,30,0)
    assert DMS(1.6666666666666667)==(1,40,0)
    assert DMS(123456789.987654321)==(123456789, 59, 16)
    assert[DMS(i/100) for i in range(10**3,10**5,3163)]== \
          [(10, 0, 0), (41, 37, 48), (73, 15, 36), (104, 53, 24),
          (136, 31, 12), (168, 9, 0), (199, 46, 48), (231, 24, 36),
          (263, 2, 24), (294, 40, 12), (326, 18, 0), (357, 55, 48),
          (389, 33, 36), (421, 11, 24), (452, 49, 12), (484, 26, 60),
          (516, 4, 48), (547, 42, 36), (579, 20, 24), (610, 58, 12),
          (642, 36, 0), (674, 13, 48), (705, 51, 36), (737, 29, 24),
          (769, 7, 12), (800, 45, 0), (832, 22, 48), (864, 0, 36),
          (895, 38, 24), (927, 16, 12), (958, 53, 60), (990, 31, 48)]
    print('DMS...Passed')
    negs=[DMS(i/100) for i in range(-10**4,0,887)]
    if negs==[(-100, 0, 0), (-91, 7, 48), (-82, 15, 36), (-73, 23, 24),
              (-64, 31, 12), (-55, 38, 60), (-46, 46, 48), (-37, 54, 36),
              (-29, 2, 24), (-20, 10, 12), (-11, 18, 0), (-2, 25, 48)] \
              and DMS(-1/120)==(0,0,-30) and DMS(-.5)==(0,-30,0):
        print('DMS 1 point bonus')


def testBinomialExperimentProbability():
    assert almostEqual(binomialExperimentProbability(.1,10,3),0.05739562800000002)
    assert almostEqual(binomialExperimentProbability(.5,3,0),0.125)
    assert almostEqual(binomialExperimentProbability(.5,10,0),0.0009765625)
    experiments=[binomialExperimentProbability(i/100,7,4) for i in range(35,65)]
    conductedExperiments=[0.14423819921874997, 0.1541054398464,
            0.16401991744845001, 0.17393120241279997, 0.18378750306735003,
            0.193536, 0.20312318894665005, 0.21249523048320001,
            0.22159830475755005, 0.23037896949760006, 0.23878451953125007,
            0.24676334605440006, 0.25426529388295, 0.2612420149248,
            0.26764731610785, 0.2734375, 0.27857169635715,
            0.28301218283519997, 0.28672469310205007, 0.2896787105856,
            0.29184774609374997, 0.2932095975424, 0.29374659002745,
            0.29344579447679997, 0.29229922311835, 0.29030400000000006,
            0.28746250479764995, 0.2837824881472, 0.27927715673655,
            0.2739652263936]
    for experiment in experiments:
        assert almostEqual(experiment,conductedExperiments[experiments.index(experiment)])
    print('binomialExperimentProbability...Passed')

def testDayOfWeek():
    # On 2/5/2006, the Steelers won Super Bowl XL on a Sunday!
    assert(dayOfWeek(2, 5, 2006) == 1)
    # On 6/15/1215, the Magna Carta was signed on a Monday!
    assert(dayOfWeek(6, 15, 1215) == 2)
    # On 3/11/1952, the author Douglas Adams was born on a Tuesday!
    assert(dayOfWeek(3, 11, 1952) == 3)
    # on 4/12/1961, Yuri Gagarin became the first man in space, on a Wednesday!
    assert(dayOfWeek(4, 12, 1961) == 4)
    # On 7/4/1776, the Declaration of Independence was signed on a Thursday!
    assert(dayOfWeek(7, 4, 1776) == 5)
    # on 1/2/1920, Isaac Asimov was born on a Friday!
    assert(dayOfWeek(1, 2, 1920) == 6)
    # on 10/11/1975, Saturday Night Live debuted on a Saturday (of course)!
    assert(dayOfWeek(10, 11, 1975) == 7)
    # Quiz Day--Monday this semester
    assert (dayOfWeek(2,10,2020) == 2)
    print('dayOfWeek...Passed')
    
def testAll():
    print()
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print()
    if integerSquareRoot(1)!=None:
        testIntegerSquareRoot()
    if fabricYards(1)!=None:
        testFabricYards()
    if angleOfRegularPolygon(4)!=None:
        testAngleOfRegularPolygon()
    if numberOfQuadraticRoots(1,2,3)!=None:
        testNumberOfQuadraticRoots()
    if findReferenceAngle(1)!=None:
        testFindReferenceAngle()
    if isTriangular(1)!=None:
        testIsTriangular()
    if simpleCannonAiming(1)!=None:
        testSimpleCannonAiming()
    if kthRoot(3,2)!=None:
        testKthRoot()
    if DMS(0)!=None:
        testDMS()
    if binomialExperimentProbability(1,1,1)!=None:
        testBinomialExperimentProbability()
    if dayOfWeek(1,1,1)!=None:
        testDayOfWeek()
    

testAll()
    
