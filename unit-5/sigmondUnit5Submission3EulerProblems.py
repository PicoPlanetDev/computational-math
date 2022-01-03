import math
import datetime

def almostEqual(x,y):
    return abs(x-y)<10**-8

def euler31():
	target = 200 # count by indivdual pence
	coins = [1,2,5,10,20,50,100,200] # list of pence values to use
	ways = [1] + [0] * target # generate list starting with 1 and as many 0s as target
	# Go through every coin and find the ways available to make the target
	for coin in coins:
		for i in range(len(ways) - coin):
			ways[i + coin] += ways[i]
	return ways[-1] # return the last value in the list

def euler33(low, high):
	numer = 1 # start with basic fraction
	denom = 1 # start with basic fraction
	# Go through all possible combinations of numerator and denominator with two digits
	for d in range(low, high):
		for n in range(10, d):
			n0 = n % 10
			n1 = n // 10
			d0 = d % 10
			d1 = d // 10
			# Identify the "non trivial"cases
			if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
				numer *= n
				denom *= d
	return denom // math.gcd(numer, denom) # return the value of the denominator of the products

def euler34():
	factorials = []
	# Generate a list of factorials
	for i in range(10):
		factorials.append(math.factorial(i))

	# have to nest this function because it uses the pre-generated factorials list for speed
	def sumFactorialDigits(n):
		sumDigits = 0
		# Until the number is 0
		while n:
			sumDigits += factorials[n % 10]
			n //= 10
		return sumDigits

	total = 0

	# loop to a really big number for the upper bound
	for i in range(10,1000000):
		if sumFactorialDigits(i) == i:
			total += i

	return total

pointTotal = 0

print('Euler #31', euler31(), '5pts')
pointTotal += 5
print('Euler #33', euler33(10,100), '6pts')
pointTotal += 6
print('Euler #34', euler34(), '10pts')
pointTotal += 6

print()
print('Euler Problems Score...', pointTotal, "pts/50 pts")