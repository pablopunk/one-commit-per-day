#!/usr/bin/python

dim = 20

def factorial(n):
    f = 1
    for x in range(1, n+1): f *= x
    return f

paths = factorial(dim*2) / factorial(dim) / factorial(dim)

print 'Grid %dx%d:' % (dim,dim) , 'Paths:', paths
