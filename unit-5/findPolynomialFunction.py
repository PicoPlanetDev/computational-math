import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

# Ensure that matplotlib, numpy are installed
# pip install matplotlib or pip3 install matplotlib
# pip install numpy or pip3 install numpy

def almostEqual(x,y):
    return abs(x-y)<10**-8

def gaussianElimination(m):
    def pivot(m, n, i):
        max_row = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[max_row] = m[max_row], m[i]

    # forward elimination
    n = len(m[0])
    for i in range(n):
        pivot(m, n, i)
        for j in range(i+1, n):
            m[j] = [m[j][k] - m[i][k]*m[j][i]/m[i][i] for k in range(n+1)]

    if m[n-1][n-1] == 0: raise ValueError('No unique solution')

    # backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        s = sum(m[i][j] * x[j] for j in range(i, n))
        x[i] = (m[i][n] - s) / m[i][i]
    return x


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
# Mr. Jackson, can you help me figure out how to make it work if there are zero points? as in intercepts?
# If you go down to line 106 and change fitPolynomial to fitPolynomialGaussian, it will fail when dividing by zero

def fitPolynomialGaussian(xList, yList):
    eliminationSet = []
    for i in range(len(xList)):
        eliminationSet.append([xList[i]**2, xList[i], 1, yList[i]])
    print(eliminationSet)
    variables = gaussianElimination(eliminationSet)
    print(variables)

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
    polynomial = fitPolynomialGaussian(xList, yList)
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