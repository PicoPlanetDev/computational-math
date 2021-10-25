import copy
import math
import random

def almostEqual(x,y):
    return abs(x-y)<10**-8

# Note to self for logic and stuff:
# A 2D array looks like this:
# array = [[7,8,9],
#          [4,5,6],
#          [1,2,3]]
# where each row is effectively a list of numbers
# and each column is a spot in the row's list

# Removes the row and column specified by row and col from 2D array a
def removeRowAndCol(a,r,c):
    L = copy.deepcopy(a)
    del L[r] # remove the entire row r
    for i in range(len(L)):
        del L[i][c] # remove the column c from each of the items in rows
    return L

def isMagicSquare(L):
    return None

def makeMagicSquare(n):
    return None

def findPrimitives(p):
    return None

def isLatinSquare(L):
    return None

def makeLatinSquare(n):
    return None

def matrixMultiply(m1,m2):         
    return None
   
def largestProductInAGrid(grid,p):
    return None

def smallestSumInARectangularSubGrid(grid,m,n):
    return None

def multiplyLinearFactors(F):
    return None

def powerSet(a):
    return None

def orderedPowerSet(S):
    return None

def subsetSum(a,s):
    return None

def isKnightsTour(board):
    return None

def volumeOfTetrahedron(C):
    return None

def areLegalValues(values):
    return None
       
def isLegalRow(board,row):
    return None

def isLegalCol(board,col):
    return None
            
def isLegalBlock(board,block):
    return None

def isLegalSudoku(board):
    return None

def closestDiamondToZero(s,G):
    return None

###########################################################################
A=[[135, 161, 187, 213, 239, 1, 27, 53, 79, 105, 131],
[159, 185, 211, 237, 21, 25, 51, 77, 103, 129, 133],
[183, 209, 235, 19, 23, 49, 75, 101, 127, 153, 157],
[207, 233, 17, 43, 47, 73, 99, 125, 151, 155, 181],
[231, 15, 41, 45, 71, 97, 123, 149, 175, 179, 205],
[13, 39, 65, 69, 95, 121, 147, 173, 177, 203, 229],
[37, 63, 67, 93, 119, 145, 171, 197, 201, 227, 11],
[61, 87, 91, 117, 143, 169, 195, 199, 225, 9, 35],
[85, 89, 115, 141, 167, 193, 219, 223, 7, 33, 59],
[109, 113, 139, 165, 191, 217, 221, 5, 31, 57, 83],
[111, 137, 163, 189, 215, 241, 3, 29, 55, 81, 107]]

B=[[37,	78,	29,	70,	21,	62,	13,	54,	5],
[6,     38,	79,	30,	71,	22,	63,	14,	46],
[47,	7,	39,	80,	31,	72,	23,	55,	15],
[16,	48,	8,	40,	81,	32,	64,	24,	56],
[57,	17,	49,	9,	41,	73,	33,	65,	25],
[26,	58,	18,	50,	1,	42,	74,	34,	66], 
[67,	27,	59,	10,	51,	2,	43,	75,	35],
[36,	68,	19,	60,	11,	52,	3,	44,	76],
[77,	28,	69,	20,	61,	12,	53,	4,	45]]

C=[[37,	78,	29,	70,	21,	62, 	54,	5],
[6,     38,	79,	30,	71,	22, 	14,	46],
[47,	7,	39,	80,	31,	72, 	55,	15],
[16,	48,	8,	40,	81,	32, 	24,	56],
[57,	17,	49,	9,	41,	73, 	65,	25],
[26,	58,	18,	50,	1,	42, 	34,	66], 
[67,	27,	59,	10,	51,	2,  	75,	35],
[36,	68,	19,	60,	11,	52,	44,	76]]

D=[[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]


e=[[-39, 85, 75, -20, -86, -43, -50, 65, -19, -63, -34, -63, 78, -86, -2],
[-89, 96, 27, -93, -70, -8, 1, -66, 31, 33, 70, 89, 34, -48, 94],
[-67, -35, 6, 27, -89, 6, -14, -86, -63, -95, -73, 38, -95, -16, 68],
[39, -72, 73, -49, 66, 26, -87, 3, 3, 61, -61, 36, 11, 39, -44],
[96, -75, 25, -72, 71, 92, -32, 46, -22, 32, -35, 44, 8, 51, -2],
[-36, -23, -54, 42, 32, 47, 18, -38, 100, 14, -41, -40, -14, 2, 38],
[10, 74, 51, 22, -62, -12, -5, -65, 91, 3, -74, -29, -8, 98, 48],
[-49, -35, -81, -49, 98, 75, -26, -40, 69, 54, -47, 39, -89, 34, -92],
[97, -24, 96, -31, 50, 82, 79, 19, -80, -50, -8, -97, -73, 77, -93],
[-88, 66, 40, -14, -61, 39, -43, -57, -72, -79, -86, -4, 21, 12, -87],
[-33, -25, 81, 86, -54, -96, 58, -82, 7, 81, 67, 86, -20, -8, 63],
[-95, 57, 85, -65, -99, -46, 5, 68, 80, -98, -79, 40, -93, -76, -86],
[40, 41, -87, -61, -37, -46, 11, -93, -2, 84, 100, -76, 34, -83, 35],
[-87, -15, 85, 50, -78, -51, 10, 87, 70, 55, 55, 12, -95, -1, -78],
[58, -55, -6, 67, 71, 67, 23, -96, 50, -15, 1, 61, 85, 25, 96]]



def testRemoveRowAndCol():
    global totalScore
    assert(removeRowAndCol([1],0,0)==[])
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    assert(removeRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    assert(removeRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    assert(removeRowAndCol(B,8,6)==C)
    print('removeRowAndCol...Passed...5 points')
    totalScore+=5

def testIsMagicSquare():
    global totalScore
    assert not isMagicSquare([[5,5,5],[5,5,5],[5,5,5]]) 
    assert isMagicSquare([[2,7,6],[9,5,1]])==False
    assert isMagicSquare([[2,7,6],[9,5],[4,3,9]])==False
    assert isMagicSquare([[2,7,6],3,[4,3,9]])==False
    assert isMagicSquare([])==False
    assert isMagicSquare([1,2,3,4,5,6,7,8,9])==False
    assert isMagicSquare([[2,7,6],[9,5,1],[4,3,9]])==False
    assert isMagicSquare([[2,7,6],[9,5,1],[4,3,8]])
    assert isMagicSquare([[6, 1, 8], [7, 5, 3], [2, 9, 4]])
    assert isMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
    assert isMagicSquare(A)
    assert isMagicSquare(B)
    assert isMagicSquare(C)==False
    print('isMagicSquare...Passed...10 points')
    totalScore+=10

def testMakeMagicSquare():
    global totalScore
    assert makeMagicSquare(2)==[]
    print('makeMagicSquare...Passed...15 points')
    totalScore+=15

def testFindPrimitives():
    global totalScore
    assert findPrimitives(10)==[]
    assert findPrimitives(12)==[(3,4,5)]
    assert findPrimitives(84)== [(3, 4, 5), (5, 12, 13), (8, 15, 17), \
                          (7, 24, 25), (20, 21, 29), (12, 35, 37)]
    assert findPrimitives(144)== [(3, 4, 5), (5, 12, 13), (8, 15, 17),
                    (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41),
                    (28, 45, 53), (11, 60, 61), (16, 63, 65)]
    print('findPrimitives...Passed...20 points')
    totalScore+=20

def testIsLatinSquare():
    global totalScore
    assert isLatinSquare([[1,2,3],[2,3,1],[3,1,2]])==True
    assert isLatinSquare([[1,2,3,4,5],[2,3,5,1,4],[3,5,4,2,1], \
                         [4,1,2,5,3],[5,4,1,3,2]])==True
    assert isLatinSquare([[1,2,3],[2,3,1],[3,1,5]])==False
    assert isLatinSquare([[1,2,3,4,5],[2,3,6,1,4],[3,5,4,2,1], \
                         [4,1,2,5,3],[5,4,1,3,2]])==False
    assert isLatinSquare([])==False
    assert isLatinSquare([[2,7,6],[9,5,1]])==False
    assert isLatinSquare([[2,7,6],[9,5],[4,3,9]])==False
    assert isLatinSquare([[2,7,6],3,[4,3,9]])==False
    assert isLatinSquare([])==False
    assert isLatinSquare([1,2,3,4,5,6,7,8,9])==False
    print('isLatinSquare...Passed...5 points')
    totalScore+=5

def testMakeLatinSquare():
    global totalScore
    assert isLatinSquare(makeLatinSquare(6))==True
    assert isLatinSquare(makeLatinSquare(12))==True
    print('makeLatinSquare...Passed...15 points')
    totalScore+=15

def testMatrixMultiply():
    global totalScore
    assert matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], \
                          [[9, 8, 3], [5, 1, 3]])== [[62, 31, 30], [61, 37, 27], \
                        [65, 44, 27], [75, 46, 33], [117, 73, 51], [83, 60, 33]]
    assert matrixMultiply(B,C)==[]
    if matrixMultiply([[8]],[[5]])==[[40]]:
        print('matrixMultiply...Passed...15 points')
        totalScore+=15
    else:
        assert matrixMultiply([[8]],[[5]])==[[[40]],[[40]]]
        assert matrixMultiply([[9, 8, 3], [5, 1, 3]],[[3, 7], \
                            [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]]) \
                            == [[62, 31, 30], [61, 37, 27], \
                            [65, 44, 27], [75, 46, 33], [117, 73, 51], [83, 60, 33]]
        print('matrixMultiply...Passed...25 points')
        totalScore+=25

def testLargestProductInAGrid():
    global totalScore
    assert largestProductInAGrid(B,2)==6480
    assert largestProductInAGrid(B,4)==39929760
    assert largestProductInAGrid(D,4)==70600674
    assert largestProductInAGrid(D,20)==182479798369776159130095937843200000
    print('largestProductInAGrid...Passed...25 points')
    totalScore+=25

def testSmallestSumInARectangularSubGrid():
    global totalScore
    grid=[[31, 11, 40, 32, 11, 45],
    [31, 40, 9, 11, 46, 25],
    [12, 43, 40, 28, 38, 5],
    [9, 45, 33, 24, 32, 38],
    [14, 40, 8, 39, 15, 19]]
    assert smallestSumInARectangularSubGrid(grid,1,1)==5
    assert smallestSumInARectangularSubGrid(grid,2,1)==21
    assert smallestSumInARectangularSubGrid(grid,2,3)==143
    assert smallestSumInARectangularSubGrid(grid,1,6)==135
    assert smallestSumInARectangularSubGrid(grid,5,6)==814
    print('smallestSumInARectangularSubGrid...Passed...15 points')
    totalScore+=15

def testMultiplyLinearFactors():
    global totalScore
    assert multiplyLinearFactors([[1,2],[1,3]])==[1,5,6]

    assert multiplyLinearFactors([[1,2],[1,2],[2,5],[-3,7]]) == [-6, -25, 7, 136, 140]

    print('multiplyLinearFactors...Passed...7 point')
    totalScore+=7

def testPowerSet():
    global totalScore
    a,b,c=powerSet([1,2,3]),powerSet([4,5,6,7]),powerSet([1,2,3,2])
    PS1=[[], [1], [2], [3], [1, 2], [1, 3] ,[2, 3], [1, 2, 3]]
    PS2=[[], [4], [5], [6], [7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7],
         [4, 5, 6], [4, 5, 7], [4, 6, 7], [5, 6, 7], [4, 5, 6, 7]]
    PS3=[[], [1], [2], [2], [3], [1, 2], [1, 2], [1, 3], [2, 2], [2, 3], [2, 3],
         [1, 2, 2], [1, 2, 3], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]]
    if a==PS1 and b==PS2 and c==PS3:
        print('powerSet...Ordered...Passed...20 points')
        totalScore+=20
        return
    for item in powerSet([1,2,3]):assert sorted(item) in PS1
    for item in powerSet([4,5,6,7]):assert sorted(item) in PS2
    for item in powerSet([1,2,3,2]):assert sorted(item) in PS3
    print('powerSet...Passed...10 points')
    totalScore+=10 

def testSubsetSum():
    global totalScore
    Z=subsetSum([-5, -2, 2, 3, 8],3)
    if type(Z[0])=='int':
        assert Z in [[3], [-5, 8], [-2, 2, 3], [-5, -2, 2, 8]]
        print('subsetSum...Passed...10 points')
        totalScore+=10
    else:
        assert Z==[[3], [-5, 8], [-2, 2, 3], [-5, -2, 2, 8]]
        print('subsetSum...Passed...20 points')
        totalScore+=25

def testIsKnightsTour():
    global totalScore
    a=[ [1,10,21,16,7],[20,15,8,11,22],[9,2,23,6,17],
        [14,19,4,25,12],[3,24,13,18,5]]
    b=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    assert isKnightsTour(a)
    assert not(isKnightsTour(b))
    print('isKnightsTour...Passed...15 points')
    totalScore+=15

def testVolumeOfTetrahedron():
    global totalScore
    assert volumeOfTetrahedron([(1,0,0),(0,1,0),(0,0,1),(7/3,7/3,7/3)])==1
    assert volumeOfTetrahedron([(1,0,0),(0,1,0),(0,0,1),(1,1,1)])==1/3
    print('volumeOfTetrahedron...Passed...7 points')
    totalScore+=7

def makeLegalValues(n):
    legalList=[i if random.random()>.7 else 0 for i in range(n**2)]   
    random.shuffle(legalList)
    return legalList

def testAreLegalValues():
    global totalScore
    for i in range(4,30):
        legalList=makeLegalValues(i)
        assert areLegalValues(legalList)
        if legalList[i]==0 and legalList.count(i)==1:
            legalList[i]=i
            assert not areLegalValues(legalList)       
    print('areLegalValues...Passed...5 points')
    totalScore+=5

G1=[[0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]]

G2=[[0, 0, 0, 0, 0, 0, 9, 0, 9],    #Row 0 Fails due to 9's
    [0, 0, 0, 4, 2, 0, 1, 8, 0],    #Col 8 Fails due to 9's
    [0, 0, 0, 7, 0, 5, 0, 2, 6],    #Block 2 fails due to 9's
    [1, 0, 0, 9, 0, 4, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 4, 0],
    [0, 5, 0, 5, 0, 7, 0, 0, 9],    #Row 5 Fails due to 5's
    [9, 2, 0, 1, 0, 8, 0, 0, 0],    #Col 1 fails due to 5's
    [0, 3, 4, 0, 5, 9, 0, 0, 0],    #Block 3 fails due to 5's
    [5, 0, 7, 0, 0, 0, 0, 0, 0]]

def testIsLegalRow():
    global totalScore
    for i in range(9):
        assert isLegalRow(G1,i)
        if i!=0 and i!=5: assert isLegalRow(G2,i)
    assert not isLegalRow(G2,0)
    assert not isLegalRow(G2,5)
    print('isLegalRow...Passed...2 points')
    totalScore+=2
    
def testIsLegalCol():
    global totalScore
    for i in range(9):
        assert isLegalCol(G1,i)
        if i!=1 and i!=8: assert isLegalCol(G2,i)
    assert not isLegalCol(G2,1)
    assert not isLegalCol(G2,8)
    print('isLegalCol...Passed...5 points')
    totalScore+=5

def testIsLegalBlock():
    global totalScore
    for i in range(9):
        assert isLegalBlock(G1,i)
        if i!=2 and i!=3: assert isLegalBlock(G2,i)
    assert not isLegalBlock(G2,2)
    assert not isLegalBlock(G2,3)
    print('isLegalBlock...Passed...10 points')
    totalScore+=10

def testIsLegalSudoku():
    global totalScore
    assert isLegalSudoku(G1)
    assert not isLegalSudoku(G2)
    print('isLegalSoduku...Passed...2 points')
    totalScore+=2
    
def testClosestDiamondToZero():
    global totalScore
    assert closestDiamondToZero(1,e)== [[[1]], 1]
    assert closestDiamondToZero(2,e)== [[[-81], [-24, 96, -31], [40]], 0]
    assert closestDiamondToZero(3,e)== [[[38], [-61, 36, 11], [32, -35, 44, 8, 51],
                                        [-41, -40, -14], [-29]], 0]
    assert closestDiamondToZero(4,e)== [[[-93], [6, 27, -89], [-72, 73, -49, 66, 26],
                                         [96, -75, 25, -72, 71, 92, -32], 

                                         [-23, -54, 42, 32, 47], [51, 22, -62], 

                                         [-49]], 6]
    assert closestDiamondToZero(9,e)==[]
    print('closestDiamondToZero...Passed...25 points')
    totalScore+=25

def testAll():
    if removeRowAndCol([[1,1],[1,1]],1,1)!=None:
        testRemoveRowAndCol()
        pass
    if isMagicSquare([])!=None:
        testIsMagicSquare()
        pass
    if makeMagicSquare(0)!=None:
        testMakeMagicSquare()
        pass
    if findPrimitives(0)!=None:
        testFindPrimitives()
        pass
    if isLatinSquare([])!=None:
        testIsLatinSquare()
        pass
    if makeLatinSquare(3)!=None:
        testMakeLatinSquare()
        pass
    if matrixMultiply([[0],[0]],[[1],[1]])!=None:
        testMatrixMultiply()
        pass
    if largestProductInAGrid([[1],[1]],1)!=None:
        testLargestProductInAGrid()
        pass
    if smallestSumInARectangularSubGrid([[1]],1,1)!=None:
        testSmallestSumInARectangularSubGrid()
        pass
    if multiplyLinearFactors([[1,1],[1,1]])!=None:
        testMultiplyLinearFactors()
        pass
    if powerSet([1])!=None:
        testPowerSet()
        pass
    if orderedPowerSet([[1]])!=None:
        testOrderedPowerSet()
        pass
    if subsetSum([1],0)!=None:
        testSubsetSum()
        pass
    if isKnightsTour([[1],[1]])!=None:
        testIsKnightsTour()
        pass
    if volumeOfTetrahedron([(0,0,0),(0,1,0),(0,0,1),(1,1,1)])!=None:
        testVolumeOfTetrahedron()
        pass
    if areLegalValues([1])!=None:
        testAreLegalValues()
        pass
    if isLegalRow([[1]],0)!=None:
        testIsLegalRow()
        pass
    if isLegalCol([[1]],0)!=None:
        testIsLegalCol()
        pass
    if isLegalBlock([[1]],0)!=None:
        testIsLegalBlock()
        pass
    if isLegalSudoku([[1]])!=None:
        testIsLegalSudoku()
        pass
    if closestDiamondToZero(1,[[1]])!=None:
        testClosestDiamondToZero()
        pass

totalScore=0
testAll()
print()
print('Total Score...',totalScore,' points')
