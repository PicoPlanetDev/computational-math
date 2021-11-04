import math
import time
import random
import copy

# Primes are sexy though, it goes without saying
# - Mr. Jackson
# nthSexyPrime(n)

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

def rowLength(L):
    return len(L)

def colLength(L):
    return len(L[0])

def isInteger(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def rowSum(L,r):
    return sum(L[r])

def colSum(L, c):
    total = 0
    try:
        for row in L:
            total += row[c]
        return total
    except:
        return "Col out of range"

# Flattens a 2D list into a 1D list
def flattenList(L):
    flattened = []
    for row in L:
        for col in row:
            flattened.append(col)
    return flattened

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

def isLatinSquare(L):
    if not passesSquareChecks(L): return False
    rows, cols = rowLength(L), colLength(L)
    flattened = flattenList(L)
    if rows != cols: return False
    setOfFlat = sorted(list(set(flattened)))
    for row in L:
        if setOfFlat != sorted(row): return False
    return True

def rotateList(a,n):
    return a[n:] + a[:n]

def makeLatinSquare(n):
    # List comprehension, explained outside in:
    # To end up with a square of size n, we need to make a list of n lists (outer for in in range(n))
    # Each of those lists will have n items (inner for in range(n))
    # Each of those alternates between counting down and u
    # And using modulo to wrap around the excess to the next line
    latinSquare = [[((j//2+1 if j%2 else n-j//2) + i) % n + 1 for j in range(n)] for i in range(n)]
    # If the square is odd, run through one more time with the reversed order
    if n % 2 != 0: latinSquare += [part[::-1] for part in latinSquare]
    return latinSquare

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

def volumeOfTetrahedron(C):
    a,b,c,d = C[0],C[1],C[2],C[3]
    print(a,b,c,d)
    volume = abs(dotProduct(tuple(x-y for x, y in zip(a, b)), (crossProduct(tuple(x-y for x, y in zip(b, d)), tuple(x-y for x, y in zip(c, d)))))) / 6
    return volume

#region Lists
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
#endregion

def matrixMultiply(m1,m2):
    return [[sum(a * b for a, b in zip(m1row, m2col)) for m2col in zip(*m2)] for m1row in m1]

print(matrixMultiply(B,C))