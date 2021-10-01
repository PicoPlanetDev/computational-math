import math

# Returns two lists of X and Y values from a combined list of X and Y values
def splitToXY(L):
    xList = L[::2]
    yList = L[1::2]
    return xList, yList

def linearRegression(L):
    xList, yList = splitToXY(L)
    sumX, sumY = sum(xList), sum(yList)
    n = len(xList)
    sumXY = sum([xList[i] * yList[i] for i in range(n)])
    sumX2 = sum(xList[i]**2 for i in range(n))
    slope = (sumX * sumY - (n * sumXY)) / ((sumX**2) - (n * sumX2))
    offset = (sumX * sumXY - (sumY * sumX2)) / ((sumX**2) - (n * sumX2))
    return slope, offset

print(linearRegression([0,2,1,3,2,4]))