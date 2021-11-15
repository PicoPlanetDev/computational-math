import math

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

# Some of my programs take a while, so I skip them by commenting out ones that I have already done. Please uncomment to check them.
pointTotal=0
print('Euler #1..', euler1(1000), '...passed...3pts')
pointTotal+=3
print('Euler #2..', euler2(4*10**6), '...passed...3pts')
pointTotal+=3
print('Euler #3..', euler3(600851475143), '...passed...3pts')
pointTotal+=3
print('Euler #4', euler4(100,1000), '...passed...3pts')
pointTotal+=3
print('Euler #5', euler5(1,21), '...passed...3pts')
pointTotal+=3

print()
print('Total Score...', pointTotal)