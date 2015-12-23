#!/usr/bin/python

import prime

primes = []; i=0; sol=0

while True:
    new = prime.prime(i)
    if new < 2000000: sol += new
    else: break
    i+=1

print "Solution:", sol
