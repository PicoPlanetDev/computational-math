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

# Returns the number of rows in the list
def rowLength(L):
    return len(L)

# Returns the number of columns in the first row of the list
# Or something like that, point being, if the list is ragged or jagged
# it will not be accurate for every row
def colLength(L):
    return len(L[0])

# Tests if n is an integer, or a float with no decimal places
def isInteger(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

# Sums the row r in list L
def rowSum(L,r):
    return sum(L[r])

# Sums the column c in list L
def colSum(L, c):
    total = 0
    try:
        for row in L:
            total += row[c]
        return total
    except:
        return "Col out of range"

# Sums the diagonal of a 2D array
# It is left to right if d is 0
# It is right to left if d is 1
# Kinda hacky
def diagonalSum(L, d):
    rows = rowLength(L)
    total = 0
    for i in range(rows):
        if d == 0:
            total += L[i][i]
        if d == 1:
            total += L[rows-i-1][rows-i-1]
    return total

# Flattens a 2D list into a 1D list
def flattenList(L):
    return [col for row in L for col in row]

# Returns a list of the duplicate items in a list (from Unit 3)
def duplicates(a):
    return sorted(set([x for x in a if a.count(x) > 1]))

# Basic check for isMagicSquare and isLatinSquare
def passesSquareChecks(L):
    # Ensure that list is not empty
    if L == []: return False

    # Ensure that everything in the list is a list (kind of ensures that it is 2D)
    for i in range(len(L)):
        if not isinstance(L[i], list): return False

    # Get the row and column lengths
    rows, cols = rowLength(L), colLength(L)

    # Ensures that the list is square and not jagged or ragged
    if rows != cols: return False

    # Flatten the 2D list into 1D for some checks
    flattened = flattenList(L)

    # Ensure that every element is only an integer
    for item in flattened:
        if not isInteger(item): return False

    return True

def isMagicSquare(L):
    if not passesSquareChecks(L): return False

    flattened = flattenList(L)
    # Ensure that there are no duplicates in the square
    if duplicates(flattened) != []: return False

    # Get the row and column lengths
    rows, cols = rowLength(L), colLength(L)

    # Gather row sums
    rowSums = [rowSum(L, i) for i in range(rows)]
    minRowSums, maxRowSums = min(rowSums), max(rowSums)

    # Gather column sums
    colSums = [colSum(L, i) for i in range(cols)]
    minColSums, maxColSums = min(colSums), max(colSums)

    # Gather diagonal sums
    diagSum0 = diagonalSum(L, 0)
    diagSum1 = diagonalSum(L, 1)
    
    # Recently learned you can break if statements into multiple lines like other things
    # If all the sums are equal, return true
    if minRowSums == \
       maxRowSums == \
       minColSums == \
       maxColSums == \
       diagSum0 == \
       diagSum1: return True

    # Otherwise, return false
    return False

# If n is an even number return true
def isEven(n):
    return n%2 == 0

def makeMagicSquare(n):
    # If n is not an odd number, return an empty list
    if isEven(n): return []

    # Create a 2D list of zeros
    squareList = [[0 for x in range(n)] for y in range(n)]
    
    # Create iterators for the loop
    i = n / 2
    j = n - 1

    # Start with 1
    num = 1
    # Run the loop until the square is full
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n: j = 0
            if i < 0: i = n - 1
 
        if squareList[int(i)][int(j)]:
            j = j - 2
            i = i + 1
        else:
            squareList[int(i)][int(j)] = num
            num = num + 1
 
        j = j + 1
        i = i - 1
 
    return squareList

def findPrimitives(p):
    return None

def isLatinSquare(L):
    if not passesSquareChecks(L): return False
    rows, cols = rowLength(L), colLength(L)
    flattened = flattenList(L)
    if rows != cols: return False
    setOfFlat = sorted(list(set(flattened)))
    for row in L:
        if setOfFlat != sorted(row): return False
    return True

# Pretty cool list comprehension here, most involved one I've made yet
# Creates a latin square of size n
def makeLatinSquare(n):
    # List comprehension, explained outside in:
    # To end up with a square of size n, we need to make a list of n lists (outer for in in range(n))
    # Each of those lists will have n items (inner for in range(n))
    # Each of those alternates between counting down and u
    # And using modulo to wrap around the excess to the next line
    latinSquare = [[(((b//2)+1 if (b%2 != 0) else (n-b//2)) + a) % n + 1 for b in range(n)] for a in range(n)]
    # If the square is odd, run through one more time with the reversed order
    if n % 2 != 0: latinSquare += [part[::-1] for part in latinSquare]
    return latinSquare

def matrixMultiply(m1,m2):
    m1cols = colLength(m1)
    m2rows= rowLength(m2)
    if m1cols != m2rows: return []
    return [[sum(a * b for a, b in zip(m1row, m2col)) for m2col in zip(*m2)] for m1row in m1]

def largestProductInAGrid(grid,p):
    return None

def smallestSumInARectangularSubGrid(grid,m,n):
    return None

def multiplyPolynomials(p1, p2):
    product = [0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            product[i+j]+=p1[i]*p2[j]
    return product

# Might get around to this one later
def multiplyLinearFactors(F):
    return None

def powerSet(a):
    inputList = a
    lenInputList = len(inputList)
    powerSetList = []
    # Bitwise xor (exclusive or) is used here and in the inner list
    for i in range((1*(2^lenInputList))):
        sublist = []
        for j in range(lenInputList):
            if (i & ((1*(2^j))) > 0): sublist.append(inputList[j])
        powerSetList.append(sublist)
    return powerSetList

def orderedPowerSet(S):
    # Get the power set normally
    unorderedPowerSet = powerSet(S)

    # Create a list of lengths of the sublists of the power set
    lengths = [len(x) for x in unorderedPowerSet]

    # Zip the lists (to combine the lengths and the power set)
    # Then sort the zipped list using the lengths
    # And finally drop the lengths out of the sorted zipped list
    orderedPowerSet = [x for _,x in sorted(zip(lengths,unorderedPowerSet))]
    return orderedPowerSet

def subsetSum(L,s):
    # if sum(L) == s:
    #     return L
    # if len(L) > 1:
    #     for subset in (L[:-1], L[1:]):
    #         result = subsetSum(subset, s)
    #         if result is not None:
    #             return result
    return None

def isKnightsTour(board):
    return None

def dotProduct(a,b):
    return sum(ai*bi for ai, bi in zip(a, b))

def crossProduct(a,b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return tuple(c)

#     abs((a-d) dot ((b-d) cross (c-d))
# V = ---------------------------------
#                    6
# Returns the volume of the tetrahedron formed by the points defined in C
# Based on the formula above
# Only works if test cases use ALMOST EQUAL, I reccomend modifying your test program as such
def volumeOfTetrahedron(C):
    print("Mr. Jackson, I MODIFIED THE volumeOfTetrahedron TEST CASES TO USE ALMOST EQUAL due to floating point error")
    a,b,c,d = C[0],C[1],C[2],C[3]
    volume = abs(dotProduct(tuple(x-y for x, y in zip(a, b)), (crossProduct(tuple(x-y for x, y in zip(b, d)), tuple(x-y for x, y in zip(c, d)))))) / 6
    return volume

def areLegalValues(values):
    nums = [False for x in range(len(values))]
    for n in values:
        if (n > len(values)): return False
        if (n!=0 and nums[n-1] == True): return False
        elif (n!=0): nums[n-1] = True
    return True
       
def isLegalRow(board,row):
    return areLegalValues(board[row])

def isLegalCol(board,col):
    return areLegalValues([board[i][col] for i in range(len(board))])

def isLegalBlock(board,block):
    currentBlock = []
    blockLen = round(len(board)**0.5)
    blockX = block // blockLen
    blockY = block % blockLen
    for row in range(blockX*blockLen,(blockX+1)*blockLen):
        for col in range(blockY*blockLen,(blockY+1)*blockLen):
            currentBlock.append(board[row][col])
    return areLegalValues(currentBlock)

def isLegalSudoku(board):
    for i in range(len(board)):
        if not isLegalBlock(board,i) or not isLegalRow(board,i) or not isLegalCol(board,i): return False
    return True

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
    assert almostEqual(volumeOfTetrahedron([(1,0,0),(0,1,0),(0,0,1),(7/3,7/3,7/3)]),1)
    assert almostEqual(volumeOfTetrahedron([(1,0,0),(0,1,0),(0,0,1),(1,1,1)]),1/3)
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
        testPowerSet()
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
