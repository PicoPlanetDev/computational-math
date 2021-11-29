import random
import copy
from typing import Counter

A=[[0,1,2,3],
   [5,6,7,8],
   [4,3,2,1],
   [9,8,7,6]]

B=[[1,2],[3,4],[5,6],[7,8]]

C=[[37,	        78,	29,	70,	21,	62, 	54,	5],
    [6,         38,	79,	30,	71,	22, 	14,	46],
    [47,	7,	39,	80,	31,	72, 	55,	15],
    [16,	48,	8,	40,	81,	32, 	24,	56],
    [57,	17,	49,	9,	41,	73, 	65,	25],
    [26,	58,	18,	50,	1,	42, 	34,	66], 
    [67,	27,	59,	10,	51,	2,  	75,	35],
    [36,	68,	19,	60,	11,	52,	44,	76]]

D=[[1,2,2,  4],
   [5,1,3,  4, 5,  6, 2, 8, 9],
   [7,2,13,14,15, 16,33,44,55,66,77,2,9],
   [8,9,10],
   [1,2,3,  5,55,567,44,55,66,77, 8,2]]

L=[[random.randrange(1,100)for i in range(100)] for j in range(100)]

Z=[[random.randrange(1,100)for i in range(random.randrange(50,150))] \
    for j in range(random.randrange(50,150))]

def greatestSumOfARow(L):
    sums = []
    for row in L:
        sums.append(sum(row))
    return max(sums)

def isRaggedList(L):
    maxrow = len(L[0])
    for row in L:
        if len(row) != maxrow:
            return True
    return False

def smallestSumOfAColumn(L):
   
    colsOfL = []
   
    for i in range(len(L[0])):
        col=[]
        for row in L:
            col.append(row[i])
        colsOfL.append(col)
   
       
    smallest = 100000000000
    rowof = 0
    if isRaggedList(colsOfL) == False:
        for i in range(len(colsOfL)):
            if sum(colsOfL[i]) < smallest:
                smallest = sum(colsOfL[i])
                rowof = i
    if isRaggedList(colsOfL) == True:
        for i in range(len(colsOfL)):
            if len(colsOfL[i]) == len(colsOfL):
                if sum(colsOfL[i]) < smallest:
                        smallest = sum(colsOfL[i])
                        rowof = i
   
   
    return (rowof, smallest)

def reverseGrid(L):
    solution=[]
    rows=[]
    i=len(L[0])-1
    count=len(L)-1
    while count>=0:
        rows.append(L[count][i])
        i-=1
        if i<0:
            solution.append(rows)
            count-=1
            rows=[]
            i=len(L[count])-1
    return solution

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 1:
        for i in range (2, int(n ** 0.5) + 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def assignAllPrimesZero(L):
    n = copy.deepcopy(L)
    for row in range(len(n)):
        for column in range(len(n[row])):
            if isPrime(n[row][column]):
                n[row][column] = 0
    return n



def searchForPythagoreanTriples(L):
    solution=[]
    tup=[]
    count=0
    while count<len(L):
        for i in range(len(L[count])-3):
            tup1=[L[count][i],L[count][i+1],L[count][i+2]]
            tup=sorted(tup1)
            tup=tuple(tup)
            if (tup[0]**2)+(tup[1]**2)==(tup[2]**2):
                tup1=tuple(tup1)
                solution.append([tup1,(count,i)])
        count+=1
    return solution

# Flattens a 2D list into a 1D list
def flattenList(L):
    return [col for row in L for col in row]

def occurenceOfEachNumber(L):
    numbers = [0 for i in range(99)]
    flat = flattenList(L)
    for num in flat:
        numbers[num-1] += 1
    labels = [i+1 for i in range(99)]
    combined = []
    for i in range(99):
        combined.append((labels[i], numbers[i]))
    for i in range(10):
        print(combined[10*i:10*(i+1)])
    return numbers

#Not fully finished
def removeRowsAndColsMedianFifty(L):
    n = copy.deepcopy(L)
    cols = []
    for i in range(len(n[0])):
        colly = []
        for j in range(len(n)):
            colly.append(n[j][i])
        cols.append(colly)

    for row in range(len(n)):
        for col in range(len(n[row])):
            if statistics.median(n[row]) == 50:
                n.pop(n[row])
            if statistics.median(n[row][col]) == 50:
                n.pop(n[row[col]])
    return n

def longestIncreasingSequence(L):
    return None

print('Results for L')
print('Greatest Sum in any Row...=',greatestSumOfARow(L))
print('Smallest Sum in any Column...=',smallestSumOfAColumn(L))
print('Reversed Grid Equal to Approved Solution...')
print('Assign all Primes in Grid to Zero Equal to Approved Solution...')
print('Pythagorean Triples in a Row...',searchForPythagoreanTriples(L))
print('Occurence of each digit in the Grid', end='...')
occurenceOfEachNumber(L)
print('Remove Row & Col with Median=50....')
print('longestIncreasingSequence...',longestIncreasingSequence(L))
print()
print('Results for Z')
print('Greatest Sum in any Row...=',greatestSumOfARow(Z))
print('Smallest Sum in any Column...=',smallestSumOfAColumn(Z))
print('Reversed Grid Equal to Approved Solution...',reverseGrid(Z))
print('Assign all Primes in Grid to Zero',assignAllPrimesZero(Z))
print('Assign all Primes in Grid to Zero',assignAllPrimesZero(Z))
print('Pythagorean Triples in a Row...',searchForPythagoreanTriples(Z))
print('Occurence of each digit in the Grid', end='...')
occurenceOfEachNumber(Z)
print('Remove Row & Col with Median=50....',removeRowsAndColsMedianFifty(Z))
print('longestIncreasingSequence...',longestIncreasingSequence(Z))



