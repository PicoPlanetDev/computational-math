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

def isMagicSquare(L):
    #print(L)
    if L == []: return False
    for i in range(len(L)):
        if not isinstance(L[i], list): return False
    rows = rowLength(L)
    cols = colLength(L)
    if rows != cols: return False
    for i in range(len(L)):
        for j in range(len(L[i])):
            if not isInteger(L[i][j]): return False

    rowSums = []
    for i in range(rows):
        rowSums.append(rowSum(L,i))
    colSums = []
    for j in range(cols):
        colSums.append(colSum(L,j))
    for rowsum in rowSums:
        #print(rowsum)
        if not rowsum == 15: return False
    for colsum in colSums:
        #print(colsum)
        if not colsum == 15: return False
    return True

print(isMagicSquare([[2,7,6],[9,5,1],[4,3,8]]))
print(isMagicSquare([[5,5,5],[5,5,5],[5,5,5]]))