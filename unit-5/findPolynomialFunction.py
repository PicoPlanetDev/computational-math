import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

# Ensure that matplotlib, numpy are installed
# pip install matplotlib or pip3 install matplotlib
# pip install numpy or pip3 install numpy

def almostEqual(x,y):
    return abs(x-y)<10**-8

# This is probably going to be slow because 
# I haven't used numpy in a while and don't feel like looking up the docs
# So it just uses normal lists
def gaussianElimination(M):
    matrix = deepcopy(M)
    # Iterate through rows and columns in the array
    for col in range(len(matrix[0])):
        for row in range(col+1, len(matrix)):
            # Calculate a new row value for each combination, putting these in list currentRow
            currentRow = [(rowValue * (-(matrix[row][col] / matrix[col][col]))) for rowValue in matrix[col]]
            matrix[row] = [sum(pair) for pair in zip(matrix[row], currentRow)] # Find the sum of each pair of row values and the r calculated above
    # When I learned elimination, 
    # we had to the find the other variables by putting them back in
    # to "find Grandma"
    variablesSolution = [] # Create a list to represent the solution
    matrix.reverse() # If we iterate through matrix backwards we can make it easier
    for equationSolution in range(len(matrix)):
            if equationSolution == 0:
                variablesSolution.append(matrix[equationSolution][-1] / matrix[equationSolution][-2])
            else:
                inner = 0
                for x in range(equationSolution):
                    inner += (variablesSolution[x]*matrix[equationSolution][-2-x])
                # If the equation is in y=mx+b form
                # We can rearrange it to solve for x like this:
                # x = (y-b)/m
                variablesSolution.append((matrix[equationSolution][-1]-inner)/matrix[equationSolution][-equationSolution-2])
    variablesSolution.reverse() # Because we used a reversed input matrix, we need to reverse the output
    # Remove floating point error by rounding each solution to 8 decimal places
    # 8 is somewhat arbitrary but almostEqual uses 10**-8 so that what I picked
    for i in range(len(variablesSolution)):
        variablesSolution[i] = round(variablesSolution[i], 8)
    return variablesSolution

def splitTupleToXY(L):
    x,y = map(list,zip(*L))
    return x, y

def evalPolynomial(coeffs, x):
    return sum(coeff*x**i for i,coeff in enumerate(coeffs[::-1]))

def checkValues(xList, yList, coeffs):
    for i in range(len(xList)):
        if not almostEqual(evalPolynomial(coeffs, xList[i]), yList[i]):
            return False
    return True

def fitPolynomial(xList, yList):
    degree = 0
    while True:
        fit = np.polynomial.polynomial.polyfit(xList, yList, degree) # Numpy is way more efficient than python for analysing lists
        fit = np.flip(fit) # Fit is reversed at first, as in c + bx + ax^2, which is not so useful, so we use flip() to fix it
        if checkValues(xList, yList, fit):
            return fit
        degree += 1

# Some points
# (1,3)
# (2,6)
# (3,14)
# Now set up some equations
# a(1)**2 + b(1) + c = 3
# a(2)**2 + b(2) + c = 6
# a(3)**2 + b(3) + c = 14
# Now solve the system using gaussian elimination
# Use these values to identify the polynomial
# This only works if there are no zeros in the input function
# Mr. Jackson, can you help me figure out how to make it work if there are zero points?
# def fitPolynomialGaussian(xList, yList):
#     eliminationSet = []
#     for i in range(len(xList)):
#         eliminationSet.append([xList[i]**2, xList[i], 1, yList[i]])
#     print(eliminationSet)
#     variables = gaussianElimination(eliminationSet)
#     print(variables)

def graphPolynomialFunction(P, xStep, xStart, xEnd, xPoints, yPoints):
    xList = []
    x = xStart
    while x <= xEnd:
        xList.append(x)
        x += xStep
    yList = [evalPolynomial(P, x) for x in xList]

    plt.plot(xList, yList, c="blue")

    plt.scatter(xPoints, yPoints, c="orange")

    plt.show()

def findPolynomialFunction(D):
    xList, yList = splitTupleToXY(D)
    polynomial = fitPolynomial(xList, yList)
    print(polynomial)
    xListSorted, yListSorted = splitTupleToXY(sorted(D))
    graphPolynomialFunction(polynomial, 0.1, xListSorted[0]-1, yListSorted[-1]+1, xList, yList)
    return polynomial

A = [(0,6), (-2,0), (-3,0)]
B = [(-3,5280.5),(-2,675.4),(-1,27.2),(4,17732.2),(1,41.8),(2,470.6),(3,3500.4)]
D = [(1,3),(2,6),(3,14)]
#xList, yList = splitTupleToXY(A)
#print(fitPolynomial(xList, yList))
findPolynomialFunction(A)