# Copyright Pablo Varela, 2016
# From http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110201&format=html
#
# A sequence of n > 0 integers is called a jolly jumper
# if the absolute values of the differences between successive
# elements take on all possible values 1 through n - 1. For instance:
#
# 1 4 2 3
#
# is a jolly jumper, because the absolute differences are 3, 2, and 1,
# respectively. The definition implies that any sequence of a single
# integer is a jolly jumper.

def isJolly(seq):
    n = len(seq)
    if n==1: return 1 # 1 element -> is jolly jumper by definition
    subs = []
    subs = list( abs(seq[x] - seq[x+1]) for x in range(0, n-1))
    for i in range(0, n-1):
        if subs[i] != n-i-1: return 0
    return 1

print "Sequence: ",
numbers = raw_input().replace(" ", "")
seq = list(int(n) for n in numbers)

if isJolly(seq): print "Jolly"
else: print "Not Jolly"
