#!/usr/bin/python

dim = 20
paths = 0
grid = [[1 for x in range(dim+1)] for x in range(dim+1)]

def right(x, y):
	if x+1 <= dim: return 1 # can go right
	return 0

def down(x, y):
	if y+1 <= dim: return 1 # can go down
	return 0

def explore(x, y):
	global paths
	if right(x, y): explore(x+1, y)
	if down (x, y): explore(x, y+1)
	if x == dim and y == x: paths += 1

explore(0,0)

print 'Grid %dx%d:' % (dim,dim) , 'Paths:', paths
