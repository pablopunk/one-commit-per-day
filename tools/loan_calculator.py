# Copyright Pablo Varela, 2016
# From http://openbookproject.net/pybiblio/practice/wilson/loan.php
# The interest due on a loan can be calculated
# according to the simple formula:
#
# I = P x R x T
#
# where I is the interest paid, P is the amount
# borrowed (principal), R is the interest rate,
# and T is the length of the loan.

print "\nLoan calculator\n"

print "Amount borrowed: ",
P = float(raw_input())
print "Interest rate: ",
R = float(raw_input())/100.0
print "Term (years): ",
T = int(raw_input())

I = P * R * T

print "\nAmount borrowed:\t$%.2f" % P
print "Total interest paid:\t$%.2f" % I
