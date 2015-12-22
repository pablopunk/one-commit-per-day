#!/usr/bin/python

maxNum = 1000 # how much we are searching
a = 0; b = 0; c = 0

for i in range(1, maxNum): # a
    for j in range(i, maxNum): # b
        k = 1000 - i - j # c from a+b+c=1000
        if i*i + j*j == k*k:
            a = i; b = j; c = k
            break

print "Solution:",a*b*c
