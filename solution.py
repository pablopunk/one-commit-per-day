#!/usr/bin/python

# This whole commit was made on iPad

from math import sqrt

def factors(n):    
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

def triangle(nth):
	return sum(x for x in range(1, nth+1))
	
divisors=0; n=2

while divisors < 500:
	n += 1
	divisors = len(factors(triangle(n)))
	
print 'Solution:',triangle(n)
