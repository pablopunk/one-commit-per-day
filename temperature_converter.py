#!/usr/bin/python
# Copyright Pablo Varela, 2016
# Exercise from http://openbookproject.net/pybiblio/practice/wilson/tempfinder.php

def toF(C):
    return (C*9.0/5.0)+32

def toC(F):
    return (5.0/9.0)*(F-32)

print "Temperature Converter"
print "\nEnter a temperature: ",
t = int(raw_input())
c = ''
while c.lower() not in ('c', 'f'):
    print "Convert to (F)ahrenheit or (C)elsius?: ",
    c = raw_input()
c = c.lower()
if c == 'c': print t,"F =",toC(t),"C"
if c == 'f': print t,"C =",toF(t),"F"
