# Copyright Pablo Varela 2016
#
# This is a simple game where you have to
# travel through a matrix and try to reach the
# final cell without touching any bomb
#

try:
    __import__("getch")
except ImportError:
    print "You need getch() to run this program"
    print "https://pypi.python.org/pypi/getch"
    exit()

from os import system
from random import random
from time import sleep
from getch import getch

# clear screen
def cls():
    system("clear")

bomb_prob = 0
dim = 0
matrix = [[0 for x in range(dim)] for x in range(dim)]
x,y = 0,0

# TODO: choose among 3 levels of dificulty
# (b) beginner (a) advanced (i) impossible

def init():
    global dim, bomb_prob, matrix, x, y
    bomb_prob = 0.1
    dim = 20
    matrix = [[0 for x in range(dim)] for x in range(dim)]
    x,y = 0,0
    # bombs
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = (1 and random()<bomb_prob)
    # TODO: be sure there's a path to the end without bombs
    matrix[0][0] = 0

def printMatrix():
    isbomb = False
    for i in range(dim):
        for j in range(dim):
            if x == i and y == j:
                if matrix[i][j]:
                    print "X",
                    isbomb = True
                else:
                    print "@",
            else: print "-",
        print ""
    return isbomb

cls()
print "\n\tWelcome to BombPath\n"
print "\tUse WASD to move and reach the"
print "\tlast cell of the matrix."
print "\tIt's not that easy"
print "\n\t[PRESS ENTER]\n"
getch()

init()

while True:
    cls()
    b = printMatrix()
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
