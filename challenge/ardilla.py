#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# matrix
# 1 0 0 0
# 0 1 0 0
# 1 0 1 0
# 0 1 0 1
#

N = 3
M = 3
K = 2
node_count = 0
nodes = []
visited = []
trees  = [[1,1], [2,2], [2,0], [3,1]]
n = 0
#trees = [[3,0], [0,3]]
matrix = []
adj_matrix = []
last_tree = []

# get node number from coors
def node_from_coord(i,j):
    for n in nodes:
        if i==n[0][0] and j==n[0][1]:
            return n[1]
    return -1

# get coords from node number
def coord_from_node(node):
    for n in nodes:
        if n[1] == node:
            return n[0][0],n[0][1]
    return -1,-1

# returns an array of achievable neighbors
def get_neighs(i,j):
    neighs = []
    
    rows = range(i-K, i+K+1)
    cols = range(j-K, j+K+1)
    
    for i1 in rows:
        if i1>=0 and i1 <= N:
            for j1 in rows:
                if j1>=0 and j1 <= N:
                    if matrix[i1][j1]:
                        if i1!=i or j1!=j:
                            # print "new neigh of %i,%i is %i,%i" % (i,j,i1,j1)
                            neighs.append([i1,j1])

    return neighs

# returns true or false
def is_end_achievable(x):
    # print coord_from_node(x)
    if x == node_from_coord(N,M): return True # last node

    global visited
    visited.append(x)
    i=0; achievable=False
    for num in adj_matrix[x]:
        if num and i not in visited:
            if is_end_achievable(i): achievable = True
        i+=1

    return achievable

# graph constructor
def fill_adj_matrix():
    global adj_matrix
    adj_matrix = [[0 for x in range(n+2)] for y in range(n+2)]
    for i in range(0,N+1):
        for j in range(0,M+1):
            if matrix[i][j]:
                neighs = get_neighs(i,j)
                for k in neighs:
                    x,y = node_from_coord(i,j),node_from_coord(k[0],k[1])
                    adj_matrix[x][y] = 1
                    adj_matrix[y][x] = 1

# set node number for each coord
def assign_nodes_to_coords():
    global node_count,nodes
    node_count = 0
    nodes=[]

    for i in range(0,N+1):
        for j in range(0,M+1):
            if matrix[i][j]:
                c = [i,j]
                nodes.append([c,node_count])
                node_count+=1
    # for n in nodes:
    #     print "%i,%i is node %i" % (n[0][0],n[0][1],n[1])

# fills tree matrix
def fill_matrix():
    global matrix
    matrix = [[0 for x in range(N+1)] for y in range(M+1)]
    for tree in trees:
        matrix[tree[0]][tree[1]] = 1 # place tree
    matrix[0][0] = 1 # first tree
    matrix[N][M] = 1 # last tree
    print "[ Matrix ]"
    for i in matrix:
        for j in i:
            print j,
        print ""

# removes a tree
def remove_tree():
    global last_tree
    last_tree = trees.pop(0)
    print "Removing tree", last_tree

# initial setup
def reset():
    global visited,n
    visited = []
    n = len(trees)
    
    fill_matrix()
    assign_nodes_to_coords()
    fill_adj_matrix()

def main():
    reset()

    while True:
        if is_end_achievable(0):
            print "-> Is achievable"
            remove_tree(); reset()
        else:
            if not last_tree:  print "-> Never achievable"
            else: print "-> Not achievable when removing", last_tree
            break

if __name__ == '__main__':
    main()