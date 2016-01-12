#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Pablo Varela 2016
#
# This is a simple game where you have to
# travel through a matrix and try to reach the
# final cell without touching any bomb
#

from os import system
from random import random
from time import sleep

try:
    __import__("getch")
except ImportError:
    print "You need getch() to run this program"
    sleep(0.2)
    print "Trying to install it..."
    sleep(0.2)
    if system("bash -c 'su -c \"curl https://raw.githubusercontent.com/pablopunk/one-commit-per-day/master/tools/install_getch.sh && chmod +x install_getch.sh && ./install_getch.sh && rm install_getch.sh\"'"):
        print "\nError! Check one of this sources to get it:"
        print "\t- https://raw.githubusercontent.com/pablopunk/one-commit-per-day/master/tools/install_getch.sh"
        print "\t- https://pypi.python.org/pypi/getch"
        exit()

from getch import getch

# clear screen
def cls():
    system("clear")

bomb_prob = 0
dim = 0
matrix = [[0 for x in range(dim)] for x in range(dim)]
x,y = 0,0
debug = False

def bombs():
    global matrix,dim
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = (1 and random()<bomb_prob)
    # TODO: be sure there's a path to the end without bombs
    matrix[0][0] = 0
    matrix[dim-1][dim-1] = 0

def init(d):
    global dim, bomb_prob, matrix, x, y
    bomb_prob = d
    dim = 20
    matrix = [[0 for x in range(dim)] for x in range(dim)]
    x,y = 0,0
    bombs()

def printMatrix(debug = False):
    isbomb = False
    for i in range(dim):
        for j in range(dim):
            if x == i and y == j:
                if matrix[i][j]:
                    print "*",
                    isbomb = True
                else:
                    print "@",
            else:
                if debug and matrix[i][j]:
                    print "x",
                else: print "·",
        print ""
    return isbomb

cls()
print "\n\tWelcome to BombPath\n"
print "\tUse WASD to move and reach the"
print "\tlast cell of the matrix."
print "\n\tChoose level:"
print "\tBegginer(b)\tAdvanced(a)\tImpossible(i):",
c = getch().lower()
d = 0.02
while c not in ['b', 'a', 'i']:
    print "\n\n\tWhat's that?: ",
    c = getch().lower()
if c == 'a': d = 0.09
elif c == 'i': d = 0.2

init(d)

def main_loop():
    global x,y, debug
    cls() # clear screen
    print ""
    b = printMatrix(debug)
    if x == dim-1 and y == dim-1:
        print "\n\tYOU WON!"
        print "\n\tWas it worth it?\n"; exit()
    if b:
        print "\n\tBOMB!"
        print "\n\tTry again.\n"; exit()
    k = getch().lower()
    if k == "w" and x > 0: x -= 1;
    elif k == "a" and y > 0: y -= 1;
    elif k == "s" and x < dim-1: x += 1;
    elif k == "d" and y < dim-1: y += 1;
    elif k == "c": debug = not debug;

while True:
    main_loop()
