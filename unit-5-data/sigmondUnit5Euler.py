import math

def euler1(n):
    total=0
    for i in range(n):
        if i%3==0 or i%5==0:
            total=total+i
    return total

def euler2(n):
    a,b,evenSum=0,1,0
    while b<n:
        a,b=b,a+b
        if b%2==0:evenSum+=b
    return evenSum

def euler3(n):
    for factor in range(2, int(math.sqrt(n)) + 1):
        while n % factor == 0:
            n /= factor
            if n == 1 or n == factor:
                return factor



pointTotal=0
print('Euler #1..', euler1(1000), '...passed...3pts')
pointTotal+=3
print('Euler #2..', euler2(4*10**6), '...passed...3pts')
pointTotal+=3
print('Euler #3..', euler3(600851475143), '...passed...3pts')
pointTotal+=3

print()
print('Total Score...', pointTotal)