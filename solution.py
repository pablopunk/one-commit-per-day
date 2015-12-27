#!/usr/bin/python

cache = { 1:1 } # n - size

def getcache(cache, n):
    cache[n] = cache.get(n, 0) or (n%2==0 and 1+getcache(cache, n/2) or 1+getcache(cache, 3*n+1)) # calm down, you DO understand it
    return cache[n]

largest,ln = 0,0
for n in range(13, 1000000):
    new = getcache(cache, n)
    if largest < new:
        largest, ln = new, n # updates max

print "Solution:",ln
