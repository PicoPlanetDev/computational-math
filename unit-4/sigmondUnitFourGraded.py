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
###   Grading Test Cases
###########################################################################
###########################################################################

import random
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


def testRemoveRowAndCol():
    global totalScore
    assert(removeRowAndCol([1],0,0)==[])
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    assert(removeRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    assert(removeRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    Z=copy.deepcopy(B)
    assert(removeRowAndCol(B,8,6)==C)
    assert B==Z
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
    assert not isMagicSquare([[7 ,6, 2], [5, 1, 9], [3 ,8, 4]])
    assert isMagicSquare(A)
    assert not isMagicSquare(A.pop(0))
    assert isMagicSquare(B)
    assert not isMagicSquare(C)
    x,y=random.randint(1000,10000),random.randint(20,30)
    z=[[x]*y for i in range(y)]
    assert not isMagicSquare(z)
    print('isMagicSquare...Passed...10 points')
    totalScore+=10

def testMakeMagicSquare():
    global totalScore
    assert makeMagicSquare(10)==[]
    for i in range(1,99,2):
        x=makeMagicSquare(i)
        for row in x:assert sum(row)==sum([row[0] for row in x])
        assert len(x)*[sum(row)]==[sum([x[row][col] for row in range(len(x))]) for col in range(len(x))]
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
    assert findPrimitives(1000)==[(3, 4, 5), (5, 12, 13), (8, 15, 17),
            (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
            (11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73), (13, 84, 85),
            (36, 77, 85), (39, 80, 89), (20, 99, 101), (65, 72, 97),
            (15, 112, 113), (60, 91, 109), (44, 117, 125), (17, 144, 145),
            (24, 143, 145), (88, 105, 137), (51, 140, 149), (85, 132, 157),
            (19, 180, 181), (52, 165, 173), (119, 120, 169), (57, 176, 185),
            (28, 195, 197), (104, 153, 185), (95, 168, 193), (21, 220, 221),
            (84, 187, 205), (133, 156, 205), (60, 221, 229), (140, 171, 221),
            (32, 255, 257), (105, 208, 233), (23, 264, 265), (120, 209, 241),
            (69, 260, 269), (96, 247, 265), (115, 252, 277), (68, 285, 293),
            (25, 312, 313), (160, 231, 281), (36, 323, 325), (161, 240, 289),
            (75, 308, 317), (136, 273, 305), (207, 224, 305), (27, 364, 365),
            (204, 253, 325), (76, 357, 365), (175, 288, 337), (180, 299, 349),
            (40, 399, 401), (225, 272, 353), (135, 352, 377), (29, 420, 421),
            (152, 345, 377), (252, 275, 373), (189, 340, 389), (120, 391, 409),
            (87, 416, 425), (228, 325, 397), (84, 437, 445), (145, 408, 433),
            (31, 480, 481)]
    import time
    start=time.time()
    z=findPrimitives(10**5)
    assert len(z)==7026
    if time.time()-start>.1:
        print('findPrimitives...Passed...15 points')
        totalScore+=15
        return
    start=time.time()
    zz=findPrimitives(10**6)
    assert len(zz)==70229
    if time.time()-start<1:
        print('findPrimitives...Passed... 20 points')
        totalScore+=20
        return
    print('findPrimitives...Passed...15 points')
    totalScore+=15

E=[[1, 2, 30, 3, 29, 4, 28, 5, 27, 6, 26, 7, 25, 8, 24, 9, 23, 10, 22, 11, 21, 12, 20, 13, 19, 14, 18, 15, 17, 16],
   [2, 3, 1, 4, 30, 5, 29, 6, 28, 7, 27, 8, 26, 9, 25, 10, 24, 11, 23, 12, 22, 13, 21, 14, 20, 15, 19, 16, 18, 17],
   [3, 4, 2, 5, 1, 6, 30, 7, 29, 8, 28, 9, 27, 10, 26, 11, 25, 12, 24, 13, 23, 14, 22, 15, 21, 16, 20, 17, 19, 18],
   [4, 5, 3, 6, 2, 7, 1, 8, 30, 9, 29, 10, 28, 11, 27, 12, 26, 13, 25, 14, 24, 15, 23, 16, 22, 17, 21, 18, 20, 19],
   [5, 6, 4, 7, 3, 8, 2, 9, 1, 10, 30, 11, 29, 12, 28, 13, 27, 14, 26, 15, 25, 16, 24, 17, 23, 18, 22, 19, 21, 20],
   [6, 7, 5, 8, 4, 9, 3, 10, 2, 11, 1, 12, 30, 13, 29, 14, 28, 15, 27, 16, 26, 17, 25, 18, 24, 19, 23, 20, 22, 21],
   [7, 8, 6, 9, 5, 10, 4, 11, 3, 12, 2, 13, 1, 14, 30, 15, 29, 16, 28, 17, 27, 18, 26, 19, 25, 20, 24, 21, 23, 22],
   [8, 9, 7, 10, 6, 11, 5, 12, 4, 13, 3, 14, 2, 15, 1, 16, 30, 17, 29, 18, 28, 19, 27, 20, 26, 21, 25, 22, 24, 23],
   [9, 10, 8, 11, 7, 12, 6, 13, 5, 14, 4, 15, 3, 16, 2, 17, 1, 18, 30, 19, 29, 20, 28, 21, 27, 22, 26, 23, 25, 24],
   [10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1, 20, 30, 21, 29, 22, 28, 23, 27, 24, 26, 25],
   [11, 12, 10, 13, 9, 14, 8, 15, 7, 16, 6, 17, 5, 18, 4, 19, 3, 20, 2, 21, 1, 22, 30, 23, 29, 24, 28, 25, 27, 26],
   [12, 13, 11, 14, 10, 15, 9, 16, 8, 17, 7, 18, 6, 19, 5, 20, 4, 21, 3, 22, 2, 23, 1, 24, 30, 25, 29, 26, 28, 27],
   [13, 14, 12, 15, 11, 16, 10, 17, 9, 18, 8, 19, 7, 20, 6, 21, 5, 22, 4, 23, 3, 24, 2, 25, 1, 26, 30, 27, 29, 28],
   [14, 15, 13, 16, 12, 17, 11, 18, 10, 19, 9, 20, 8, 21, 7, 22, 6, 23, 5, 24, 4, 25, 3, 26, 2, 27, 1, 28, 30, 29],
   [15, 16, 14, 17, 13, 18, 12, 19, 11, 20, 10, 21, 9, 22, 8, 23, 7, 24, 6, 25, 5, 26, 4, 27, 3, 28, 2, 29, 1, 30],
   [16, 17, 15, 18, 14, 19, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 7, 26, 6, 27, 5, 28, 4, 29, 3, 30, 2, 1],
   [17, 18, 16, 19, 15, 20, 14, 21, 13, 22, 12, 23, 11, 24, 10, 25, 9, 26, 8, 27, 7, 28, 6, 29, 5, 30, 4, 1, 3, 2],
   [18, 19, 17, 20, 16, 21, 15, 22, 14, 23, 13, 24, 12, 25, 11, 26, 10, 27, 9, 28, 8, 29, 7, 30, 6, 1, 5, 2, 4, 3],
   [19, 20, 18, 21, 17, 22, 16, 23, 15, 24, 14, 25, 13, 26, 12, 27, 11, 28, 10, 29, 9, 30, 8, 1, 7, 2, 6, 3, 5, 4],
   [20, 21, 19, 22, 18, 23, 17, 24, 16, 25, 15, 26, 14, 27, 13, 28, 12, 29, 11, 30, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5],
   [21, 22, 20, 23, 19, 24, 18, 25, 17, 26, 16, 27, 15, 28, 14, 29, 13, 30, 12, 1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6],
   [22, 23, 21, 24, 20, 25, 19, 26, 18, 27, 17, 28, 16, 29, 15, 30, 14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7],
   [23, 24, 22, 25, 21, 26, 20, 27, 19, 28, 18, 29, 17, 30, 16, 1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8],
   [24, 25, 23, 26, 22, 27, 21, 28, 20, 29, 19, 30, 18, 1, 17, 2, 16, 3, 15, 4, 14, 5, 13, 6, 12, 7, 11, 8, 10, 9],
   [25, 26, 24, 27, 23, 28, 22, 29, 21, 30, 20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10],
   [26, 27, 25, 28, 24, 29, 23, 30, 22, 1, 21, 2, 20, 3, 19, 4, 18, 5, 17, 6, 16, 7, 15, 8, 14, 9, 13, 10, 12, 11],
   [27, 28, 26, 29, 25, 30, 24, 1, 23, 2, 22, 3, 21, 4, 20, 5, 19, 6, 18, 7, 17, 8, 16, 9, 15, 10, 14, 11, 13, 12],
   [28, 29, 27, 30, 26, 1, 25, 2, 24, 3, 23, 4, 22, 5, 21, 6, 20, 7, 19, 8, 18, 9, 17, 10, 16, 11, 15, 12, 14, 13],
   [29, 30, 28, 1, 27, 2, 26, 3, 25, 4, 24, 5, 23, 6, 22, 7, 21, 8, 20, 9, 19, 10, 18, 11, 17, 12, 16, 13, 15, 14],
   [30, 1, 29, 2, 28, 3, 27, 4, 26, 5, 25, 6, 24, 7, 23, 8, 22, 9, 21, 10, 20, 11, 19, 12, 18, 13, 17, 14, 16, 15]]

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
    assert isLatinSquare(E)
    for i in range(len(E)):
        c=copy.deepcopy(E)
        c[random.randrange(0,30)][random.randrange(0,30)]=99
        assert not isLatinSquare(c)
        
    print('isLatinSquare...Passed...5 points')
    totalScore+=5

def testMakeLatinSquare():
    global totalScore
    x=[makeLatinSquare(i) for i in range(10,100,2)]
    for z in x:assert [sorted(z[0])]*len(z)==[sorted(row) for row in z]
    for y in x:
        z=[[y[row][col] for row in range(len(y))] for col in range(len(y))]
        assert [sorted(z[0])]*len(z)==[sorted(row) for row in z]
    print('makeLatinSquare...Passed...15 points')
    totalScore+=15
    

def testMatrixMultiply():
    global totalScore
    a=[[-2, -83, -54, 69, -38, 69, -42, 46, 4, -29],
       [87, 56, -69, -46, 97, 5, -90, 33, -5, -91],
       [36, -21, -85, 44, 44, -12, 99, 23, 32, 74],
       [14, 47, -87, 80, -1, 67, -80, -17, 32, -43],
       [9, 54, -42, 82, 79, 98, 13, 40, -14, -51],
       [27, 8, -15, 3, -9, 83, 85, 24, -49, 57],
       [95, 75, 13, -24, 6, -59, 13, 35, -62, 43]]
    b=[[97, 31, -84, -3, -14, 54, 11], [-96, -14, 95, -6, 76, -95, -68],
       [73, 15, 26, -20, -86, 13, 99]]
    assert matrixMultiply(b,a)== \
           [[1814, -4191, -55, 81, -5898, 10116, -10389, 4725, -5683, -7456],
            [-6031, 3151, -4054, 5299, 12927, -4661, 7206, -4211, 10341, -869],
            [10797, -3820, -743, -5498, -6472, -9730, 1032, 5128, -5162, 8686]]
    assert matrixMultiply([[3, 7], [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]], \
                          [[9, 8, 3], [5, 1, 3]])== [[62, 31, 30], [61, 37, 27], \
                        [65, 44, 27], [75, 46, 33], [117, 73, 51], [83, 60, 33]]
    assert matrixMultiply(B,C)==[]
    if matrixMultiply([[8]],[[5]])==[[40]]:
        assert matrixMultiply(a,b)==[]
        assert 17911234==sum([sum(row) for row in matrixMultiply(D,D)])
        print('matrixMultiply...Passed...15 points')
        totalScore+=15
    else:
        assert matrixMultiply([[8]],[[5]])==[[[40]],[[40]]]
        assert matrixMultiply([[9, 8, 3], [5, 1, 3]],[[3, 7], \
                            [4, 5], [5, 4], [5, 6], [8, 9], [7, 4]]) \
                            == [[62, 31, 30], [61, 37, 27], \
                            [65, 44, 27], [75, 46, 33], [117, 73, 51], [83, 60, 33]]
        assert matrixMultiply(b,a)== \
           [[1814, -4191, -55, 81, -5898, 10116, -10389, 4725, -5683, -7456],
            [-6031, 3151, -4054, 5299, 12927, -4661, 7206, -4211, 10341, -869],
            [10797, -3820, -743, -5498, -6472, -9730, 1032, 5128, -5162, 8686]]
        assert 17911234==sum([sum(row) for row in matrixMultiply(D,D)[0]])
        assert 17911234==sum([sum(row) for row in matrixMultiply(D,D)[1]])
        print('matrixMultiply...Passed...25 points')
        totalScore+=25

def makeTestGrid(row,col):
    s=290797
    grid=[]
    for i in range(row):
        row=[]
        for j in range(col):
            s=s*s%50515093
            row.append(s%500)
        grid.append(row)
    return grid

def testLargestProductInAGrid():
    global totalScore
    z=makeTestGrid(125,30)
    if largestProductInAGrid(D,4)==70600674:
        if largestProductInAGrid(D,20)!=182479798369776159130095937843200000:
                print('largestProductInAGrid...Euler #11 only...15 points')
                totalScore+=15
                return
    assert largestProductInAGrid(B,2)==6480
    assert largestProductInAGrid(B,4)==39929760
    assert largestProductInAGrid(D,4)==70600674
    assert largestProductInAGrid(D,20)==182479798369776159130095937843200000
    otherTestCases=[largestProductInAGrid(z,i) for i in range(5,31,5)]
    otherSolutions=[21154755859776, 200560178926764169999200000,
     1155341158053481157811076602369792000000,
     378412546161264652150154240894113086970638336000000,
     1098843259568149148897624204883419465320979798056413989437440000,
     93449276515704711219510008924875437541033967012581262047051776000000000000]
    for i in range(len(otherTestCases)):
        if otherTestCases[i]!=otherSolutions[i]:
            print('largestProductInAGrid...Passed the Euler Grid case but failed on z...20pts')
            totalScore+=20
            return
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
    assert smallestSumInARectangularSubGrid(D,15,10)==6809
    assert smallestSumInARectangularSubGrid(D,20,20)==18934
    x=makeTestGrid(150,50)
    assert [25537, 30439, 35498, 27396, 32431, 37506, 29264, 34592, 40145]== \
    [smallestSumInARectangularSubGrid(x,i,j) for i in range(21,24) for j in range(6,9)]
    print('smallestSumInARectangularSubGrid...Passed...15 points')
    totalScore+=15

def testMultiplyLinearFactors():
    global totalScore
    assert multiplyLinearFactors([[1,2],[1,3]])==[1,5,6]
    assert multiplyLinearFactors([[1,2],[1,2],[2,5],[-3,7]]) == [-6, -25, 7, 136, 140]
    assert multiplyLinearFactors([[2,5]]*10)== \
           [1024, 25600, 288000, 1920000, 8400000, 25200000,
            52500000, 75000000, 70312500, 39062500, 9765625]
    print('multiplyLinearFactors...Passed...7 points')
    totalScore+=7

def testPowerSet():
    global totalScore
    a,b,c,d=powerSet([1,2,3]),powerSet([4,5,6,7]),powerSet([1,2,3,2]), \
             powerSet([5,1,3,9,2])
    PS1=[[], [1], [2], [3], [1, 2], [1, 3] ,[2, 3], [1, 2, 3]]
    PS2=[[], [4], [5], [6], [7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7],
         [4, 5, 6], [4, 5, 7], [4, 6, 7], [5, 6, 7], [4, 5, 6, 7]]
    PS3=[[], [1], [2], [2], [3], [1, 2], [1, 2], [1, 3], [2, 2], [2, 3], [2, 3],
         [1, 2, 2], [1, 2, 3], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]]
    PS4=[[], [1], [2], [3], [5], [9], [1, 2], [1, 3], [1, 5], [1, 9], [2, 3],
         [2, 5], [2, 9], [3, 5], [3, 9], [5, 9], [1, 2, 3], [1, 2, 5],
         [1, 2, 9], [1, 3, 5], [1, 3, 9], [1, 5, 9], [2, 3, 5], [2, 3, 9],
         [2, 5, 9], [3, 5, 9], [1, 2, 3, 5], [1, 2, 3, 9], [1, 2, 5, 9],
         [1, 3, 5, 9], [2, 3, 5, 9], [1, 2, 3, 5, 9]]
    if a==PS1 and b==PS2 and c==PS3 and d==PS4:
        print('powerSet...Ordered...Passed...20 points')
        totalScore+=20
        return
    for item in powerSet([1,2,3]):assert sorted(item) in PS1
    for item in powerSet([4,5,6,7]):assert sorted(item) in PS2
    for item in powerSet([1,2,3,2]):assert sorted(item) in PS3
    for item in powerSet([5,1,3,9,2]):assert sorted(item) in PS4
    print('powerSet...Passed...10 points')
    totalScore+=10    


def testIsKnightsTour():
    global totalScore
    a=[[38,41,18, 3,22,27,16, 1],[19, 4,39,42,17, 2,23,26],[40,37,54,21,52,25,28,15],
    [ 5,20,43,56,59,30,51,24],[36,55,58,53,44,63,14,29],[ 9, 6,45,62,57,60,31,50],
    [46,35, 8,11,48,33,64,13],[ 7,10,47,34,61,12,49,32]]
    b=[[38,41,18, 3,22,27,16, 1],[19, 4,39,42,17, 2,23,26],[40,37,54,21,52,25,28,15],
    [ 5,20,43,56,59,30,51,24],[36,55,58,53,44,63,14,29],[ 6, 9,45,62,57,60,31,50],
    [46,35, 8,11,48,33,64,13],[ 7,10,47,34,61,12,49,32]]
    c=[[29, 4,57,24,73, 6,95,10,75, 8],[58,23,28, 5,94,25,74, 7,100,11],
    [ 3,30,65,56,27,72,99,96, 9,76],[22,59, 2,63,68,93,26,81,12,97],
    [31,64,55,66, 1,82,71,98,77,80],[54,21,60,69,62,67,92,79,88,13],
    [49,32,53,46,83,70,87,42,91,78],[20,35,48,61,52,45,84,89,14,41],
    [33,50,37,18,47,86,39,16,43,90],[36,19,34,51,38,17,44,85,40,15]]
    d=[[29, 4,57,24,73, 6,95,10,75, 8],[58,23,28, 5,94,25,74, 7,100,11],
    [ 3,30,65,56,27,72,99,96, 9,76],[22,59, 2,63,68,93,26,81,12,97],
    [31,64,55,66, 1,82,71,98,88,80],[54,21,60,69,62,67,92,79,77,13],
    [49,32,53,46,83,70,87,42,91,78],[20,35,48,61,52,45,84,89,14,41],
    [33,50,37,18,47,86,39,16,43,90],[36,19,34,51,38,17,44,85,40,15]]
    e=[[43, 4,49,92,45, 6,47,198,193, 8,195,208,269,10,221,210,279,12,219,212],
    [50,89,44, 5,48,185,192, 7,196,207,266, 9,222,209,278,11,220,211,282,13],
    [ 3,42,93,154,91,46,197,190,199,194,205,270,273,268,223,280,283,316,213,218],
    [88,51,90,157,184,191,186,203,206,265,242,267,226,277,272,315,224,281,14,317],
    [41, 2,153,94,155,166,189,200,233,204,227,274,271,314,225,284,325,318,217,214],
    [52,87,156, 1,158,183,202,187,228,241,264,243,276,285,330,319,312,215,326,15],
    [37,40,95,152,165,188,167,232,201,234,275,260,331,262,313,352,329,324,311,216],
    [86,53,38,159,128,169,182,229,240,259,244,263,286,343,332,341,320,351,16,327],
    [39,36,127,96,151,164,231,168,235,180,239,334,261,340,353,350,363,328,323,310],
    [54,85,116,105,160,129,170,181,230,245,258,287,344,333,342,357,354,321,362,17],
    [35,82,97,126,117,150,163,236,179,238,335,252,339,356,349,364,359,368,309,322],
    [84,55,104,115,106,161,130,171,246,253,288,257,336,345,358,355,366,361,18,369],
    [81,34,83,98,125,118,149,162,237,178,251,338,289,348,365,360,381,370,367,308],
    [56,77,110,103,114,107,124,131,172,247,254,249,256,337,346,371,386,307,380,19],
    [33,80,99,76,109,132,119,148,123,250,177,290,347,372,385,382,379,398,387,306],
    [78,57,74,111,102,113,108,137,176,173,248,255,374,295,378,397,388,383,20,399],
    [61,32,79,100,75,120,133,122,147,138,291,174,297,396,373,384,377,400,305,390],
    [58,69,60,73,112,101,66,139,136,175,146,143,294,375,296,395,392,389,302,21],
    [31,62,71,68,29,64,121,134,27,144,141,292,25,298,393,376,23,300,391,304],
    [70,59,30,63,72,67,28,65,140,135,26,145,142,293,24,299,394,303,22,301]]
    assert isKnightsTour(a)
    assert not(isKnightsTour(b))
    assert isKnightsTour(c)
    assert not(isKnightsTour(d))
    assert isKnightsTour(e)
    print('isKnightsTour...Passed...15 points')
    totalScore+=15
        
def testSubsetSum():
    global totalScore
    Z=subsetSum([-5, -2, 2, 3, 8],3)
    W=subsetSum([-5, -2, 2, 3, 8,-4,1,7,2,-6],6)
    X=[[-2, 8], [-5, 3, 8], [-4, 2, 8], [-4, 2, 8], [-4, 3, 7], [-2, 1, 7],
       [1, 2, 3], [1, 2, 3], [-6, 1, 3, 8], [-6, 2, 2, 8], [-6, 2, 3, 7],
       [-6, 2, 3, 7], [-5, -4, 7, 8], [-5, 1, 2, 8], [-5, 1, 2, 8],
       [-5, 1, 3, 7], [-5, 2, 2, 7], [-4, 1, 2, 7], [-4, 1, 2, 7],
       [-6, -5, 2, 7, 8], [-6, -5, 2, 7, 8], [-6, -4, 1, 7, 8],
       [-6, 1, 2, 2, 7], [-5, -2, 2, 3, 8], [-5, -2, 2, 3, 8],
       [-4, -2, 1, 3, 8], [-4, -2, 2, 2, 8], [-4, -2, 2, 3, 7],
       [-4, -2, 2, 3, 7], [-2, 1, 2, 2, 3], [-6, -4, -2, 3, 7, 8],
       [-6, -2, 1, 2, 3, 8], [-6, -2, 1, 2, 3, 8], [-6, -2, 2, 2, 3, 7],
       [-5, -4, -2, 2, 7, 8], [-5, -4, -2, 2, 7, 8], [-5, -4, 2, 2, 3, 8],
       [-5, -2, 1, 2, 2, 8], [-5, -2, 1, 2, 3, 7], [-5, -2, 1, 2, 3, 7],
       [-4, -2, 1, 2, 2, 7], [-6, -5, -2, 1, 3, 7, 8], [-6, -5, -2, 2, 2, 7, 8],
       [-6, -4, -2, 1, 2, 7, 8], [-6, -4, -2, 1, 2, 7, 8],
       [-6, -4, 1, 2, 2, 3, 8], [-5, -4, 1, 2, 2, 3, 7],
       [-6, -5, -4, 1, 2, 3, 7, 8], [-6, -5, -4, 1, 2, 3, 7, 8],
       [-6, -5, -4, -2, 1, 2, 2, 3, 7, 8]]
    if isinstance (Z[0],int) and isinstance(W[0],int):
        assert Z in [[3], [-5, 8], [-2, 2, 3], [-5, -2, 2, 8]]
        assert W in X
        print('subsetSum...Passed...10 points')
        totalScore+=10
    else:
        for item in Z:assert item in [[3], [-5, 8], [-2, 2, 3], [-5, -2, 2, 8]]
        assert len(Z)==len([[3], [-5, 8], [-2, 2, 3], [-5, -2, 2, 8]])
        for item in W:assert item in X
        assert len(W)==len(X)
        print('subsetSum...Passed...20 points')
        totalScore+=20

def testVolumeOfTetrahedron():
    global totalScore
    assert almostEqual(volumeOfTetrahedron([(1,0,0),(0,1,0),(0,0,1),(7/3,7/3,7/3)]),1)
    assert almostEqual(volumeOfTetrahedron([(1,0,0),(0,1,0),(0,0,1),(1,1,1)]),1/3)
    assert almostEqual(volumeOfTetrahedron([(3,4,8),(9,2,1),(5,6,11),(2,5,3)]),20)
    assert almostEqual(volumeOfTetrahedron([(-3,6,-2),(5,-8,-1),(6,2,0),(9,2,1)]),11/3)
    print('volumeOfTetrahedron...Passed...7 points')
    totalScore+=7
    
def makeLegalValues(n):
    legalList=[i if random.random()>.7 else 0 for i in range(n**2)]   
    random.shuffle(legalList)
    return legalList

def testAreLegalValues():
    global totalScore
    for i in range(4,10):
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

G3=[[0, 0, 12, 6, 0, 0, 7, 0, 18, 0, 5, 24, 0, 10, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 19, 0, 13, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 18, 5, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 3, 0, 2, 0, 0, 14, 12, 0, 16, 8, 25, 0, 0],
    [0, 16, 0, 0, 0, 2, 23, 0, 0, 13, 12, 22, 0, 0, 0, 21, 15, 19, 3, 0, 0, 0, 0, 14, 0],
    [23, 0, 24, 0, 0, 0, 0, 0, 25, 8, 4, 0, 16, 19, 21, 0, 0, 7, 0, 0, 0, 3, 12, 0, 9],
    [0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 10, 0, 24, 12, 17, 16, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 6, 25, 0, 0, 0, 8, 0, 5, 3, 0, 0, 0, 0, 0, 0, 20, 0, 0, 18, 19],
    [15, 0, 10, 11, 0, 0, 0, 18, 12, 19, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 7, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 14, 0, 22, 0, 0, 18, 16, 20, 0, 6, 11, 13, 0, 0, 0, 0, 0, 0],
    [0, 22, 0, 25, 0, 0, 1, 17, 5, 4, 7, 0, 0, 14, 0, 8, 3, 21, 0, 0, 11, 0, 0, 0, 6],
    [0, 20, 13, 15, 0, 0, 0, 0, 0, 0, 9, 0, 0, 2, 0, 25, 0, 1, 8, 0, 0, 5, 0, 21, 0],
    [0, 1, 0, 0, 0, 0, 16, 10, 0, 7, 0, 0, 4, 20, 0, 0, 9, 0, 0, 14, 0, 24, 0, 17, 0],
    [25, 2, 5, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 19, 1, 8, 0, 0],
    [0, 0, 7, 21, 0, 0, 12, 0, 2, 17, 0, 0, 0, 18, 6, 16, 0, 0, 15, 0, 0, 13, 0, 10, 0],
    [8, 10, 18, 12, 16, 9, 0, 0, 0, 5, 0, 0, 0, 0, 19, 0, 0, 17, 0, 21, 0, 15, 0, 0, 22],
    [0, 8, 0, 0, 15, 0, 3, 0, 6, 0, 21, 0, 0, 7, 0, 18, 14, 5, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 19, 0, 1, 0, 16, 11, 0, 0, 0, 10, 22, 25, 15, 0, 0, 0, 0, 0, 0, 21, 0, 0],
    [0, 3, 1, 0, 21, 0, 0, 4, 0, 0, 0, 0, 2, 0, 13, 0, 24, 25, 0, 0, 14, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 15, 0, 12, 14, 0, 6, 17, 24, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0],
    [0, 5, 23, 16, 4, 0, 13, 24, 7, 2, 0, 9, 0, 0, 15, 3, 0, 22, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 25, 20, 2, 0, 19, 0, 0, 0, 0, 1, 0, 0, 0, 0, 21, 3, 0, 0, 12, 0, 0, 0, 0],
    [16, 12, 0, 5, 0, 11, 21, 0, 23, 0, 0, 15, 0, 0, 0, 0, 19, 9, 0, 0, 0, 0, 0, 25, 10],
    [0, 0, 0, 0, 9, 20, 22, 7, 4, 0, 3, 0, 14, 25, 18, 0, 11, 0, 0, 0, 0, 0, 1, 0, 15],
    [24, 0, 6, 0, 22, 8, 0, 25, 14, 0, 10, 11, 0, 9, 0, 20, 1, 16, 0, 7, 0, 23, 0, 0, 13],
    [14, 13, 21, 1, 0, 0, 5, 0, 0, 0, 6, 0, 22, 0, 23, 10, 0, 0, 0, 2, 0, 0, 18, 7, 11]]


G4=[[24, 0, 12, 6, 0, 0, 7, 0, 18, 0, 5, 24, 0, 10, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 19, 0, 13, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 18, 5, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 3, 0, 2, 0, 0, 14, 12, 0, 16, 8, 25, 0, 0],
    [0, 16, 0, 0, 0, 2, 23, 0, 0, 13, 12, 22, 0, 0, 0, 21, 15, 19, 3, 0, 0, 0, 0, 14, 0],
    [23, 0, 24, 0, 0, 0, 0, 0, 25, 8, 4, 0, 16, 19, 21, 0, 0, 7, 0, 0, 0, 3, 12, 0, 9],
    [0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 10, 0, 24, 12, 17, 16, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 6, 25, 0, 0, 0, 8, 0, 5, 3, 0, 0, 0, 0, 0, 0, 20, 0, 0, 18, 19],
    [15, 0, 10, 11, 0, 0, 0, 18, 12, 19, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 7, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 14, 0, 22, 0, 0, 18, 16, 20, 0, 6, 11, 13, 0, 0, 0, 0, 0, 0],
    [0, 22, 0, 25, 0, 0, 1, 17, 5, 4, 7, 0, 0, 14, 0, 8, 3, 21, 0, 0, 11, 0, 0, 0, 6],
    [0, 20, 13, 15, 0, 0, 0, 0, 0, 0, 9, 0, 0, 2, 0, 25, 0, 1, 8, 0, 0, 5, 0, 21, 0],
    [0, 1, 0, 0, 0, 0, 16, 10, 0, 7, 0, 0, 4, 20, 0, 0, 9, 0, 0, 14, 0, 24, 0, 17, 0],
    [25, 2, 5, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 19, 1, 8, 0, 0],
    [0, 0, 7, 21, 0, 0, 12, 0, 2, 17, 0, 0, 0, 18, 6, 16, 0, 0, 15, 0, 0, 13, 0, 10, 0],
    [8, 10, 18, 12, 16, 9, 0, 0, 0, 5, 0, 0, 0, 0, 19, 0, 0, 17, 0, 21, 0, 15, 0, 0, 22],
    [0, 8, 0, 0, 15, 0, 3, 0, 6, 0, 21, 0, 0, 7, 0, 18, 14, 5, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 19, 0, 1, 0, 16, 11, 0, 0, 0, 10, 22, 25, 15, 0, 0, 0, 0, 0, 0, 21, 0, 0],
    [0, 3, 1, 0, 21, 0, 0, 4, 0, 0, 0, 0, 2, 0, 13, 0, 24, 25, 0, 0, 14, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 15, 0, 12, 14, 0, 6, 17, 24, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0],
    [0, 5, 23, 16, 4, 0, 13, 24, 7, 2, 0, 9, 0, 0, 15, 3, 0, 22, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 25, 20, 2, 0, 19, 0, 0, 0, 0, 1, 0, 0, 0, 0, 21, 3, 0, 0, 12, 0, 0, 0, 0],
    [16, 12, 0, 5, 0, 11, 21, 0, 23, 0, 0, 15, 0, 0, 0, 0, 19, 9, 0, 0, 0, 0, 0, 25, 10],
    [0, 0, 0, 0, 9, 20, 22, 7, 4, 0, 3, 0, 14, 25, 18, 0, 11, 0, 0, 0, 0, 0, 1, 0, 15],
    [24, 0, 6, 0, 22, 8, 0, 25, 14, 0, 10, 11, 0, 9, 0, 20, 1, 16, 0, 7, 0, 23, 0, 0, 13],
    [14, 13, 21, 1, 0, 0, 5, 0, 0, 0, 6, 0, 22, 0, 23, 10, 0, 0, 0, 2, 0, 0, 18, 7, 11]]
    #G4 fails on row 0, col 0 and block 0 due to '24'

def testIsLegalRow():
    global totalScore
    for i in range(9):
        assert isLegalRow(G1,i)
        if i!=0 and i!=5: assert isLegalRow(G2,i)
    assert not isLegalRow(G2,0)
    assert not isLegalRow(G2,5)
    for i in range(len(G3)):
        assert isLegalRow(G3,i)
        if i!=0: assert isLegalRow(G4,i)
    assert not isLegalRow(G4,0)
    print('isLegalRow...Passed...2 points')
    totalScore+=2
    
def testIsLegalCol():
    global totalScore
    for i in range(9):
        assert isLegalCol(G1,i)
        if i!=1 and i!=8: assert isLegalCol(G2,i)
    assert not isLegalCol(G2,1)
    assert not isLegalCol(G2,8)
    for i in range(len(G3)):
        assert isLegalCol(G3,i)
        if i!=0: assert isLegalCol(G4,i)
    assert not isLegalCol(G4,0)
    print('isLegalCol...Passed...5 points')
    totalScore+=5

def testIsLegalBlock():
    global totalScore
    for i in range(9):
        assert isLegalBlock(G1,i)
        if i!=2 and i!=3: assert isLegalBlock(G2,i)
    assert not isLegalBlock(G2,2)
    assert not isLegalBlock(G2,3)
    for i in range(len(G3)):
        assert isLegalBlock(G3,i)
        if i!=0: assert isLegalBlock(G4,i)
    assert not isLegalBlock(G4,0)
    print('isLegalBlock...Passed...10 points')
    totalScore+=10

def gridMaker():
    import csv
    file = open('sudoku.txt', 'r')
    csvReader = csv.reader( file,  delimiter=" ")
    rows=[item[0] for item in csvReader if item[0]!='Grid']
    grids=[rows[i:i+9] for i in range(0,len(rows),9)]
    gridLists=[[[int(char) for char in item] for item in grid] for grid in grids]
    return gridLists


def testIsLegalSudoku():
    global totalScore
    solutions=[isLegalSudoku(grid) for grid in gridMaker()]
    assert solutions==[True, True, False, True, True, True, True, True, True, \
                       True, True, True, True, True, True, False, True, True, \
                       True, True, True, True, True, True, True, True, True, \
                       True, True, True, True, True, True, True, True, True, \
                       True, False, True, True, True, True, True, True, True, \
                       True, True, False, True, True]
    print('isLegalSoduku...Passed...2 points')
    totalScore+=2

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

a=[[63, 61, -7, 37, -59, 58, 8, 58, -13, -90, -21, -40, 15, 84, -24, -58, -91, 62, 42, 26, 29, -10, -2, 77, 76, 59, -57, -99, -55, 36] ,
[55, 41, -10, -35, 87, -94, -64, -9, 37, 37, -50, 62, 17, 16, 65, -90, 39, 71, 12, -12, 46, 80, -81, 43, -11, 48, -17, 81, 59, 59] ,
[10, -37, 49, 72, 70, -38, 13, -4, 64, 57, 83, 79, -47, 25, -97, -38, 43, -84, -13, 6, -67, 46, -65, 0, -99, -33, -96, 22, 96, 28] ,
[-45, 33, -55, 16, -26, -87, -47, -9, 43, 24, 70, 44, 56, -97, -10, -54, 60, 12, 88, -56, -71, -34, -82, -92, -72, -74, 83, -76, -62, -5] ,
[-96, 38, -90, 1, -51, 58, -22, -16, -11, 28, 66, 76, 93, 26, -75, -77, -56, 8, 18, 27, -89, -9, -65, -65, 15, 86, 84, -99, 28, -44] ,
[-55, 84, 85, 69, 53, 49, 49, 99, 60, 9, -18, 79, 7, -71, -72, 82, -41, -31, -38, -77, -48, 57, -6, -82, -81, 25, 79, 90, 27, 68] ,
[67, 75, -91, 65, 30, 67, 97, -36, 28, -71, 96, 97, -16, -98, -94, 58, -10, -36, 26, -67, 43, -10, 20, 12, 39, 76, 40, -56, 59, -79] ,
[-75, 81, 75, 15, 66, 100, 61, 28, -21, 11, 55, 10, -51, 79, 5, -40, 74, -54, -23, 53, -13, 80, 6, 27, -15, 75, 51, 77, -57, 96] ,
[-18, -41, 57, -45, 33, -24, -66, -30, -35, 15, -36, 92, 93, -66, -23, -78, -62, 68, -60, -19, -17, -58, -88, -91, -86, 41, 97, -64, -96, 31] ,
[-94, 90, 98, -65, 14, -78, -56, -14, 47, 99, 33, -78, 70, 53, 4, 53, -10, 3, 10, 97, -16, 94, -22, 28, -74, 45, 23, -81, 95, -82] ,
[-17, -83, -77, 41, 95, -60, -19, -1, -61, 84, -71, 59, 30, 77, 46, -28, -43, -86, 31, -32, 29, 13, -32, -69, -13, -16, -70, -77, -6, -58] ,
[-6, -63, 7, -60, -25, -3, -22, -57, 67, 18, -33, -38, -5, -99, -40, 22, 52, -62, 96, -46, -98, 40, -81, 96, -82, -99, 24, 63, -58, 97] ,
[53, 22, -63, -10, 73, 91, 79, 68, -90, 60, 70, 84, -96, 40, 23, -93, 45, 24, 90, 7, -97, -65, -18, 92, -45, 69, 88, 51, 20, -98] ,
[78, 16, -33, 68, -94, -48, -72, 39, 21, 68, -9, -6, -78, -56, -96, -12, 62, 78, -5, 11, 7, -20, 88, 44, 98, -43, 71, 59, 79, 20] ,
[-34, -30, 80, 86, 53, -33, -41, -28, 59, 52, -30, 100, -37, 39, -86, 14, 10, -100, -72, -94, -68, 55, 57, -63, -27, -29, -11, -69, -59, -10] ,
[-70, -100, -91, -81, 63, -47, 45, -91, -32, -32, 88, -14, 57, 2, 77, -86, 100, 100, -41, 92, 58, 49, 30, -16, 17, 99, 64, -11, -52, 81] ,
[53, 11, 41, -30, 78, 55, -30, 78, 24, -51, -74, -77, 13, -27, -52, 43, 79, 69, 56, -5, -5, -46, 76, -78, -25, -77, 63, 15, -86, 16] ,
[27, 46, -4, 22, -15, -65, -13, -40, 6, 75, 99, -49, 94, 54, -45, 29, -65, -30, -81, 100, -49, 62, -29, 79, 47, 40, 50, -49, -26, 41] ,
[88, -29, -49, 3, -19, 67, -58, 40, 32, -49, 3, -29, -20, 96, -78, 40, 60, 38, -81, 86, -74, 61, -29, -87, -39, -86, -17, -50, 84, 75] ,
[-81, -65, 20, -94, 47, -96, 88, -52, 10, 21, -21, -51, -44, -35, 100, 88, -9, -90, -73, 89, -5, -28, -9, -13, 97, 16, 75, 43, 33, -58] ,
[-19, 69, -47, -39, -11, 89, -96, -96, -70, -90, 76, 97, -22, -49, -77, -29, -57, 24, 17, -27, 63, 35, 38, 92, -27, -99, 31, 78, -92, 99] ,
[34, -43, 45, -46, -2, 60, -34, 61, 11, 80, -91, -34, -26, -96, 96, -56, 61, -6, -49, -97, -17, -49, 62, 86, -20, 1, 54, 11, 33, -4] ,
[14, -29, 83, 82, 4, -76, 94, 77, -69, -26, 97, 75, -86, 16, -24, 5, -51, 98, -9, 68, 71, -26, 44, 37, 34, 7, 3, -26, 68, -65] ,
[-4, -87, -84, -75, 56, 81, -95, 17, -27, 78, -73, -33, -60, -34, 7, 65, -58, 95, -54, -23, 100, 17, 57, -93, 91, -62, 66, -61, -81, -37] ,
[0, -22, -97, 13, -24, 46, -18, -91, -20, 58, -92, -2, 50, -47, -15, -35, 85, -44, -68, 44, -90, -55, -46, -20, -42, 41, 23, 88, 86, 95] ,
[27, 34, -27, -99, -27, 57, 4, -15, 0, 82, 68, 18, 1, -5, -79, 38, -32, -54, 13, -12, -64, -84, -5, -2, 92, -57, 43, 29, -88, 27] ,
[-74, 18, 30, 9, -62, 87, -41, 83, 44, -63, -40, 62, 31, 52, 24, -71, -35, 22, -81, 71, -67, 51, 32, 86, -58, 91, -57, -23, 83, 26] ,
[81, 40, -78, -59, 5, 78, -4, 95, 42, 85, 86, 11, -95, -82, -36, -19, -72, 38, 51, 2, 81, 12, 69, 83, 51, -88, 11, -48, 92, -44] ,
[-62, 25, 99, -44, 84, 4, -12, -55, -35, 90, 24, -47, -17, 5, -65, -51, -48, -4, 38, 57, 49, -100, -52, 21, 74, -23, 37, 98, -1, -10] ,
[12, -85, -13, -15, -4, 30, -56, -4, 43, -67, 71, 84, -68, 45, -49, -79, -53, -84, 3, -71, 97, -39, 9, -36, 97, -16, 50, 66, -95, 16] ,
[92, 71, 13, -37, -91, -98, 7, 19, 36, 16, 81, -90, -22, -13, -63, 39, 44, 100, 82, 8, -36, -26, -91, -85, -46, 7, 12, 84, -26, -28] ,
[-4, 57, 35, 49, -87, -88, -95, -49, 19, -50, -9, -26, -70, 77, 95, 5, 12, -80, 45, 8, 50, 14, -91, -13, 43, -82, 60, 84, -49, -44] ,
[-85, -5, -67, 89, -92, 18, -36, 30, 33, 21, -43, -50, -75, 88, -44, 4, -18, 78, -96, 61, -34, 10, -32, -69, -84, 97, -79, -100, -99, 51] ,
[-99, -91, -20, -26, -24, 81, -70, -70, 82, -29, -56, -72, 44, 99, -86, 95, -28, -82, 67, 26, 0, -37, -9, 79, 2, 95, 16, -92, -8, 55] ,
[100, -17, -10, -100, -21, 22, 77, -28, -7, -48, -84, -5, -90, 61, 12, 62, -60, 8, 22, 18, -11, 52, 37, 59, 0, 80, -17, -3, -14, -42] ,
[-51, -23, -52, 59, 2, -84, -82, -59, -50, -87, -11, 37, 21, 22, 24, 72, -71, 100, 92, -62, -14, -29, 24, 31, -81, -74, 50, -24, 71, 75] ,
[77, 58, 79, 21, -6, 70, -92, 50, 25, 88, -26, -40, -90, -16, 50, -59, 28, -20, 76, 84, -83, 53, -45, -73, -72, 1, -6, 53, -73, -60] ,
[-49, -57, 11, -91, -41, 3, 28, 23, 88, 12, -16, -79, -17, 80, -58, 55, 92, -46, 39, -73, 58, -98, 61, -1, 92, 27, -2, 64, 33, -83] ,
[10, -30, 4, 31, 53, 59, -64, -52, 19, -79, 32, -30, -16, -100, -41, 20, 76, -2, 7, 5, -74, -95, -19, 46, -95, -98, -69, -5, 34, -9] ,
[76, 53, 85, 71, 11, -6, 35, -28, 68, -93, -44, 36, -9, 13, 30, -8, -19, -19, 91, 78, 89, -15, 0, 43, -80, -16, -26, -42, 60, 31] ,
[-93, -36, -37, -74, -11, 46, -24, 72, -27, 40, -36, 68, -76, -3, 47, -6, -57, 38, -58, 83, 80, 50, -44, 98, -25, 83, 92, -74, 39, -66] ,
[-24, 22, 43, 91, 47, -40, 84, -34, 38, 41, -68, 99, -44, 73, -52, 12, -7, 62, -32, -6, -78, -91, -97, -70, 75, -98, 24, -70, -36, 95] ,
[12, -75, 70, -96, 4, -83, -60, 95, -9, 26, -89, 17, -63, 20, -76, -14, 27, 62, -36, -6, -96, 52, -1, -37, 93, -45, -39, 12, -68, 84] ,
[-48, 61, -21, -6, 46, 15, -1, -42, -51, -20, -4, 22, 73, -10, -86, -16, 84, 42, -43, 66, -35, -22, 66, 31, 3, 19, 99, -28, 62, 20] ,
[-66, 34, -86, -86, 0, -72, 33, 58, -99, 23, -65, 42, 10, -22, -31, -37, -32, -51, 36, -84, 80, -31, 88, 11, 1, -38, -7, -28, -71, 6] ,
[58, 88, 64, -74, -28, 73, 14, -97, -18, -64, -22, 46, -12, 34, 33, 53, -63, 80, 19, -95, -17, -95, -91, 31, 2, -87, 89, 48, 42, 84] ,
[11, -45, 15, 46, 91, 37, -51, 11, -10, -57, 63, -12, -97, 58, -98, 32, 56, -17, -91, 29, -71, 70, -92, -43, -64, 74, -67, -32, -53, -3] ,
[94, 61, 36, 28, 20, 45, -77, -23, -89, 54, -79, -81, 98, 2, -49, -53, 56, 76, -58, 20, -92, -34, -31, -78, 3, 3, 39, -74, -18, -19] ,
[-23, 1, 91, -9, 6, -77, -71, 51, -50, -48, -75, -43, 23, 77, 97, -75, -17, 44, -94, 94, 95, 61, -31, 1, 17, 5, -32, -30, 16, -19] ,
[-52, -51, -19, -37, -31, 29, -22, -95, 82, 15, 31, -44, 91, 76, 19, -76, 91, 55, 54, -72, 77, 87, 94, -20, 36, -89, 34, 23, 2, 8] ,
[-35, 25, 89, 45, 1, 78, -51, 49, -80, 72, -42, -28, 84, -35, 100, -90, -2, -1, 99, -48, 81, 83, 73, 39, -40, 59, 55, -7, 51, 78] ,
[53, -8, -62, 89, 100, 9, -70, -12, -86, 53, -5, 70, 99, 31, 51, -70, 27, 85, 79, -66, 69, -73, 88, -69, -71, 27, -29, -80, 23, -46] ,
[12, -9, -29, 3, -95, -90, -71, 23, 85, 11, -45, 12, 35, -77, 1, -1, 92, 3, -47, -14, 67, 95, -46, 14, 14, 49, -95, 31, -84, 73] ,
[-65, -11, -38, 62, -53, 73, -71, -87, 81, -8, 57, -18, 77, -58, 40, 31, -17, 63, 13, -96, -38, -7, 53, -64, -78, -75, -67, 84, -16, 99] ,
[-48, -68, 64, 12, 16, 48, 10, 60, 76, -67, -71, 73, 69, 0, -31, 78, -70, -58, -91, -85, -41, -10, -34, 86, -53, -20, -73, -60, 13, -5] ,
[76, -76, 37, 99, -97, 60, 83, 71, -89, -93, -63, 50, 37, 34, 44, 3, -99, -51, 54, 71, -69, 17, -19, 73, -15, -64, 67, 99, 68, -56] ,
[12, 55, 21, 71, 50, 35, -45, -64, -95, -37, -4, -39, -1, -87, -84, -25, 9, 51, -14, 11, -10, -50, 75, 56, 25, 28, 55, -15, -52, -81] ,
[89, -90, -27, 67, -90, 37, 35, 8, -65, 52, -52, 69, -7, 51, -38, -42, -32, 54, 95, -93, 19, 27, -37, 43, -83, 54, 6, -78, -85, -85] ,
[66, 70, -25, 98, -92, -86, 4, 54, -71, -62, -46, 47, 22, -55, -6, 58, -23, -59, -71, -63, 90, 94, -39, 58, -54, 48, 26, -49, 11, -97] ,
[-41, -91, 48, 61, -7, -36, -91, 42, 27, 45, 64, 46, 82, -44, 88, -94, 46, -4, -9, 63, 99, -89, -93, -22, -55, -44, 16, 46, 78, -25] ,
[42, 25, -21, -21, 42, -30, -35, -22, -78, -33, -79, -40, 41, -73, -56, -35, 71, 49, -91, -21, 99, -84, -80, -53, -42, -45, 32, 34, 37, -32] ,
[99, -83, 78, 82, 34, 13, 10, 21, 78, 47, -40, 65, -92, 100, 53, 100, -33, -46, 66, 88, -35, 15, -12, -82, 37, 67, -7, 9, 51, -85] ,
[-59, 95, 24, -68, -83, -9, -35, -41, 90, -87, 55, 79, 84, 51, -31, 3, -26, -58, 89, -88, 63, -54, -64, 8, 63, 94, 8, 56, 34, 24] ,
[29, 87, -74, 64, -26, 5, -45, -47, -80, -70, -22, 85, 70, -7, 7, 17, 42, -100, -89, 46, 16, 81, 84, 89, -62, -32, -54, 59, 94, -28] ,
[-27, 3, -30, 26, -34, 78, 99, 95, 54, -5, -89, 31, -12, -52, 61, -25, 76, 85, 7, -24, -88, -95, -65, 13, -8, -94, 31, 96, 68, 72] ,
[85, -76, -65, -39, 3, -29, 60, 90, 97, -33, 60, -56, 55, 28, -74, -68, -15, 82, 56, -26, 20, 76, 82, -19, 13, 25, 80, 95, 52, 37] ,
[98, 7, 88, 94, -6, -16, 58, -97, -81, -24, 15, -68, 14, 50, 38, 1, 26, -96, 63, -84, 64, 100, 19, -44, 58, 75, -91, -76, 34, 20] ,
[65, -65, 1, 40, -28, 76, -1, 57, 86, -34, -31, -48, 91, -94, -97, -20, -27, -96, 92, 87, -99, 21, 64, -50, 52, -23, -52, -68, -19, -62] ,
[-8, 47, 57, -69, -95, -100, 14, -62, 94, -9, -66, 71, 77, 87, 4, -50, 20, 89, -30, -22, 2, -89, -12, -99, 4, 65, 2, -33, 40, -54] ,
[18, 46, -57, 45, -93, -8, 95, 88, -82, 18, 4, -25, -69, -1, -10, -64, -88, -39, -57, 96, 84, 32, 70, -91, -40, 62, 94, -99, 2, 62] ,
[-67, -57, 34, -44, -47, 80, 47, -48, -60, 30, -10, -37, -57, 42, 61, 92, 81, 90, -72, 86, 12, -12, -5, -68, -24, 34, -40, -97, -4, 45] ,
[-81, 84, 77, -76, 55, -11, -6, 70, -92, -71, -65, -93, -21, 70, -9, -8, 11, 87, -34, -24, 83, -55, -77, 79, -33, 13, -5, -42, -35, 3] ,
[-14, -36, 75, -71, -59, -15, 8, 17, -17, -65, -98, 86, -68, 32, -80, -80, 98, 91, 31, -38, 59, 45, -45, -32, -69, -96, 1, 30, -5, 64] ,
[18, -84, 15, -94, 28, -80, -79, 35, 70, 26, -35, -88, -55, 18, 85, 12, 39, 43, 60, 24, 22, -58, -40, 94, -58, -45, -11, -22, -52, 14] ,
[-83, -97, 10, -41, 78, 37, -20, 30, -83, -83, 54, -24, -25, -50, 48, -73, 41, 24, 27, 80, -25, 20, -38, -85, 38, -30, 17, -73, 97, -7] ,
[-74, -13, 29, -16, 29, 26, 51, 15, -76, -24, -83, -8, -37, 35, 88, -63, -3, 91, 75, 39, 97, 29, 30, 89, -21, -94, 98, -57, 80, -37] ,
[18, 47, 69, -64, -48, -43, -62, -38, 64, 14, -30, -22, 36, 98, 98, -56, -44, 47, 89, -3, -16, -39, -16, 40, 27, -37, 38, 99, 63, 7] ,
[-95, 11, 89, 55, 75, 57, 34, 99, -61, -47, -17, -100, 12, -55, 54, 17, 79, -21, 51, -57, -20, -62, -9, 71, -23, -78, -69, -91, 72, 6] ,
[40, -24, 17, 1, 21, -56, 71, 49, 25, -24, 23, -81, -63, -32, -74, -4, 52, -15, 45, -1, -61, 54, 23, 43, 83, -5, 81, -80, 10, 85] ,
[60, -19, -20, -9, -97, -94, -15, 71, -41, -34, -50, 37, 19, 99, -84, -27, -84, -58, 36, -29, -3, 91, -68, 11, 7, -5, 36, -66, 34, -14] ]


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
    assert [closestDiamondToZero(i,a)[1] for i in range(len(a[0])) \
            if closestDiamondToZero(i,a)!=[]]==[0, 0, 0, 0, 0, 0, 0, 1, -4, 0, 1, -2, 0, -6, 4]
    assert closestDiamondToZero(13,a)==[[ \
      [77],
      [-75, 88, -44],
      [-72, 44, 99, -86, 95],
      [-84, -5, -90, 61, 12, 62, -60],
      [-87, -11, 37, 21, 22, 24, 72, -71, 100],
      [25, 88, -26, -40, -90, -16, 50, -59, 28, -20, 76],
      [23, 88, 12, -16, -79, -17, 80, -58, 55, 92, -46, 39, -73],
      [-64, -52, 19, -79, 32, -30, -16, -100, -41, 20, 76, -2, 7, 5, -74],
      [-6, 35, -28, 68, -93, -44, 36, -9, 13, 30, -8, -19, -19, 91, 78, 89, -15],
      [-11, 46, -24, 72, -27, 40, -36, 68, -76, -3, 47, -6, -57, 38, -58, 83, 80, 50, -44],
      [91, 47, -40, 84, -34, 38, 41, -68, 99, -44, 73, -52, 12, -7, 62, -32, -6, -78, -91, -97, -70],
      [70, -96, 4, -83, -60, 95, -9, 26, -89, 17, -63, 20, -76, -14, 27, 62, -36, -6, -96, 52, -1, -37, 93],
      [61, -21, -6, 46, 15, -1, -42, -51, -20, -4, 22, 73, -10, -86, -16, 84, 42, -43, 66, -35, -22, 66, 31, 3, 19],
      [-86, -86, 0, -72, 33, 58, -99, 23, -65, 42, 10, -22, -31, -37, -32, -51, 36, -84, 80, -31, 88, 11, 1],
      [-74, -28, 73, 14, -97, -18, -64, -22, 46, -12, 34, 33, 53, -63, 80, 19, -95, -17, -95, -91, 31],
      [91, 37, -51, 11, -10, -57, 63, -12, -97, 58, -98, 32, 56, -17, -91, 29, -71, 70, -92],
      [45, -77, -23, -89, 54, -79, -81, 98, 2, -49, -53, 56, 76, -58, 20, -92, -34],
      [-71, 51, -50, -48, -75, -43, 23, 77, 97, -75, -17, 44, -94, 94, 95],
      [-95, 82, 15, 31, -44, 91, 76, 19, -76, 91, 55, 54, -72],
      [-80, 72, -42, -28, 84, -35, 100, -90, -2, -1, 99],
      [53, -5, 70, 99, 31, 51, -70, 27, 85],
      [-45, 12, 35, -77, 1, -1, 92],
      [-18, 77, -58, 40, 31],
      [69, 0, -31],
      [34]],
      0]
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
        #testMakeMagicSquare()
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
import time
totalScore=0
start=time.time()
testAll()
print()
print('Total Score...',totalScore,' points')
print('Elapsed Time...',time.time()-start)
