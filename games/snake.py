#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Pablo Varela 2016

from time import sleep
import sys

def pr(what):
    sys.stdout.write(what); sys.stdout.flush()

pr("Loading game")
sleep(0.5)
for i in range(3):
    pr("."); sleep(0.5)
pr(" Just kidding, there's no game\n")
sleep(2)

width = 10
for i in range(width, 1000000):
    n = i%width
    for j in range(n):
        print " ",
    print "|"
    sleep(0.05)
