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
    print "Trying to install it with 'wget' or 'curl'..."
    sleep(0.2)
    wget = "wget https://raw.githubusercontent.com/pablopunk/one-commit-per-day/master/tools/install_getch.sh -O install_getch.sh"
    curl = "curl https://raw.githubusercontent.com/pablopunk/one-commit-per-day/master/tools/install_getch.sh -o install_getch.sh"
    install = "((%s) || (%s)) && chmod +x install_getch.sh && ./install_getch.sh && rm install_getch.sh" % (wget,curl)
    if system(install):
        print "\nError! Check one of this sources to get it:"
        print "\t- https://raw.githubusercontent.com/pablopunk/one-commit-per-day/master/tools/install_getch.sh"
        print "\t- https://pypi.python.org/pypi/getch"
        exit()

from getch import getch

bomb_prob = 0
dim = 0
matrix = [[0 for x in range(dim)] for x in range(dim)]
x,y = 0,0
debug = False
mode = "Begginer"
player = "@"
cell   = "·"
bomb   = "*"
bomb2  = "x"

# clear screen
def cls():
    system("clear")

def bombs():
    global matrix,dim,x,y
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = (1 and random()<bomb_prob)
    # TODO: be sure there's a path to the end without bombs
    matrix[x][y] = 0 # current player position (0,0 at beginning)
    matrix[dim-1][dim-1] = 0

def move_bomb(matrix, x, y):
    a = int(random()*3)-1 # x and y can change -1,0,1
    b = int(random()*3)-1 #
    a += x
    b += y
    if a < 0 or a >= dim: a = x
    if b < 0 or b >= dim: b = y
    return a,b

def move_bombs(matrix):
    global dim
    newmatrix = [[0 for x in range(dim)] for x in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if matrix[i][j]:
                a,b = move_bomb(matrix,i,j)
                newmatrix[a][b] = 1
    return newmatrix

def init(d):
    global dim, bomb_prob, matrix, x, y
    bomb_prob = d
    dim = 20
    matrix = [[0 for x in range(dim)] for x in range(dim)]
    x,y = 0,0
    bombs()

def printMatrix(matrix, debug = False):
    isbomb = False
    for i in range(dim):
        for j in range(dim):
            if x == i and y == j:
                if matrix[i][j]:
                    print bomb,
                    isbomb = True; debug = True
                else:
                    print player,
            else:
                if debug and matrix[i][j]:
                    print bomb2,
                else: print cell,
        if i == dim-1: print "<- Try to reach this cell"
        else: print ""
    return isbomb

def keys():
    global dim,x,y,debug
    moved = False
    k = getch().lower()
    if k in ['w','a','s','d']: moved = True;
    if k == "w" and x > 0: x -= 1;
    elif k == "a" and y > 0: y -= 1;
    elif k == "s" and x < dim-1: x += 1;
    elif k == "d" and y < dim-1: y += 1;
    elif k == "c": debug = True;
    return moved

def main_loop():
    global dim,x,y,debug,d,mode,matrix
    cls() # clear screen
    print "\nMode:",mode
    if debug and mode!="Random": print "YOU ARE CHEATING :("
    b = printMatrix(matrix, debug)
    if mode == "Random": matrix = move_bombs(matrix)
    if x == dim-1 and y == dim-1:
        print "\n\tYOU WON!"
        print "\n\tWas it worth it?\n"
        return True
    if b:
        print "\n\tBOMB!"
        print "\n\tTry again.\n"
        return True
    moved = keys() # input
    while not moved: moved = keys() # if the player doesn't move...

def main():
    global mode,debug
    cls()
    print "\n\tWelcome to BombPath\n"
    print "\tUse WASD to move and reach the"
    print "\tlast cell of the matrix."
    print "\n\tBegginer(b)\n\tAdvanced(a)\n\tImpossible(i)\n\tRandom(r)"
    print "\n\tChoose level:",
    c = getch().lower()
    d = 0.02
    while c not in ['b', 'a', 'i', 'r']:
        print "\n\n\tWhat's that?: ",
        c = getch().lower()
    if c == 'a': d = 0.09; mode = "Advanced"
    elif c == 'i': d = 0.2; mode = "Impossible"
    elif c == 'r': d = 0.09; debug = True; mode = "Random"

    init(d)

    exit = False
    while not exit:
        exit = main_loop()

if __name__ == '__main__':
    main()
