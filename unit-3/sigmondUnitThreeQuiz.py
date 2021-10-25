import random
import math

L=[random.randrange(2,10**6)for i in range(10**6)]


def sumOfNumbersLessThan1000(L):
    return sum([i for i in L if i < 1000])

def addAlternateOpposites(L):
    A = []
    for i in range(len(L)-1):
        A.append(L[i]-L[i+1])
    return sum(A)

def findPerfectSquares(L):
    squares = []
    for i in range(len(L)):
        if math.sqrt(L[i]) % 2 == 0:
            squares.append(L[i])
    return sorted(squares)

def findMultiplesOf93157(L):
    multiples = []
    for i in range(len(L)):
        if L[i] % 93157 == 0:
            multiples.append(L[i])
    return sorted(multiples)

# Returns true if n is a prime number
def isPrime(n):
    if (n < 2): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    for factor in range(3,round(n**0.5)+1,2):
        if (n % factor == 0): return False
    return True

def findNumberOfPrimes(L):
    print("Please wait. No time bonus on primes for me")
    count = 0
    for i in range(len(L)):
        if isPrime(L[i]):
            count += 1
    return count

def findCarolNumbers(L):
    carols = []
    for x in range(11):
        if ((2**x-1)**2-2) in L:
            carols.append(L[L.index((2**x-1)**2-2)])
    return carols

def fibonacciNumbersInList(L):
    fibonacci_numbers = [0, 1]
    for i in range(2,32):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    fibsInList=[i for i in L if i in fibonacci_numbers]
    return list(set(sorted(fibsInList)))

def largestDivisibleByNextItem(L):
    return 'Not accomplished'

def reverseNumber(n):
    num = n
    reverse = 0
    while(num>0):
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num//10
    return reverse

def isPalindromic(n):
    return n == reverseNumber(n)

def numberOfPalindromes(L):
    count = 0
    for i in range(len(L)):
        if L[i] == reverseNumber(L[i]):
            count += 1
    return count

# All the below functions are copied from previous units for numbersWithAllSixDigits:
# Returns the kth digit of n counting from the right  
def kthDigit(n, k):
    return int(abs(n) // (10**k) % 10)

# Returns the number of digits in n
def digitCount(n):
    n=abs(n)
    counter=0
    while True:
        n//=10
        counter+=1
        if (n==0): return counter

# Returns true if n includes the digit d somewhere
def doesInclude(n, d):
    for i in range(digitCount(n)):
        if kthDigit(n, i) == d: return True
    return False

# A version of isPandigital that checks 1-6 digits
def isSixPandigital(n):
    for i in range(1,6):
        if not doesInclude(n, i): return False
    return True

def numbersWithAllSixDigits(L):
    print("Please wait, numbersWithAllSixDigits is very slow. Maybe 5-10 seconds")
    numbers = [i for i in L if isSixPandigital(i)]
    return len(numbers)

print('Sum of Numbers in L less than 1000...=',sumOfNumbersLessThan1000(L))
print('Sum of first-second+third+-fourth+fifth...=',addAlternateOpposites(L))
print('Number of Perfect Squares...=',len(findPerfectSquares(L)))
print('All multiples of 93157...',findMultiplesOf93157(L))
print('Number of Primes in the list...=',findNumberOfPrimes(L))
print('All Carol numbers in the list...',findCarolNumbers(L))
print('Fibonacci Numbers in the List...=',fibonacciNumbersInList(L))
print('Largest member divisible by the next item...=',largestDivisibleByNextItem(L))
print('Number of Palindromes in the list...=',numberOfPalindromes(L))
print('Number of Members of L with each digit 1-6 used exactly once...=',numbersWithAllSixDigits(L))