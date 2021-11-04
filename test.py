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
#endregion

def matrixMultiply(m1,m2):
    r=[]
    m=[]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums=0
            for k in range(len(m2)):
                sums=sums+(m1[i][k]*m2[k][j])
            r.append(sums)
        m.append(r)
        r=[]
    return m

print(matrixMultiply(B,C))