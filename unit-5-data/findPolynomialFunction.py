import numpy as np
import matplotlib.pyplot as plt

# Ensure that matplotlib, numpy are installed
# pip install matplotlib or pip3 install matplotlib
# pip install numpy or pip3 install numpy

def almostEqual(x,y):
    return abs(x-y)<10**-8

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
findPolynomialFunction(A)