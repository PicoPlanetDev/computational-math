import math
import tkinter as tk

def almostEqual(x,y):
    return abs(x-y)<10**-8

# Free
def euler1(n):
    total=0
    for i in range(n):
        if i%3==0 or i%5==0:
            total=total+i
    return total

# Free
def euler2(n):
    a,b,evenSum=0,1,0
    while b<n:
        a,b=b,a+b
        if b%2==0:evenSum+=b
    return evenSum

# Largest prime factor
def euler3(n):
    for factor in range(2, int(math.sqrt(n)) + 1):
        while n % factor == 0:
            n /= factor
            if n == 1 or n == factor:
                return factor

# Heler for isPalindromic
def reverseNumber(n):
    num = n
    reverse = 0
    while(num>0):
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num//10
    return reverse

# Helper for euler4
def isPalindromic(n):
    return n == reverseNumber(n)

# Using Unit 2 isPalindromic
def euler4(lower, upper):
	return max(i * j for i in range(lower, upper) for j in range(lower, upper) if isPalindromic(i * j))

# Uses floor division
def euler5(lower, upper):
    num = 1
    for i in range(lower, upper):
        num *= (i // math.gcd(i, num))
    return num

def euler144():
    int result = 0;
    
    double xA = 0.0;
    double yA = 10.1;
    
    double xO = 1.4;
    double yO = -9.6;
    
    while(xO > 0.01 || xO < -0.01 || yO < 0){
    
        //Calculate the slope of A
        double slopeA = (yO - yA) / (xO - xA);
    
        //Calculate the slope of the ellipse tangent
        double slopeO = -4*xO/yO;
    
        //Calculate the slope of B
        double tanA = (slopeA - slopeO)/(1+slopeA*slopeO);
        double slopeB = (slopeO- tanA)/ (1+ tanA*slopeO);
    
        //calculate intercept of line B
        double interceptB = yO - slopeB * xO;
    
        //solve the quadratic equation for finding
        // the intersection of B and the ellipse
        // a*x^2 + b*x + c = 0
        double a = 4 + slopeB*slopeB;
        double b = 2 * slopeB * interceptB;
        double c = interceptB * interceptB - 100;
    
        double ans1 = (-b + Math.Sqrt(b * b - 4 * a * c)) / (2 * a);
        double ans2 = (-b - Math.Sqrt(b * b - 4 * a * c)) / (2 * a);
    
        xA = xO;
        yA = yO;
    
        //Take the solution which is furtherst from x0
        xO = (Math.Abs(ans1 - xO) > Math.Abs(ans2 - xO)) ? ans1 : ans2;
        yO = slopeB * xO + interceptB;
    
        result++;
    }


# Some of my programs take a while, so I skip them by commenting out ones that I have already done. Please uncomment to check them.
pointTotal=0
print('Euler #1', euler1(1000), '3pts')
pointTotal+=3
print('Euler #2', euler2(4*10**6), '3pts')
pointTotal+=3
print('Euler #3', euler3(600851475143), '3pts')
pointTotal+=3
print('Euler #4 takes a while.')
print('Euler #4', euler4(100,1000), '3pts')
pointTotal+=3
print('Euler #5', euler5(1,21), '3pts')
pointTotal+=3

print()
print('Euler Problems Score...', pointTotal)