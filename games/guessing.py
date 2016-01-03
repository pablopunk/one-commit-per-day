# Copyright Pablo Varela 2016
# From http://openbookproject.net/pybiblio/practice/wilson/guessinggame.php
#
# Example output:
#
# Time to play a guessing game.
#
# Enter a number between 1 and 100: 62
# Too high. Try again: 32
# Too low. Try again: 51
# Too low. Try again: 56
#
# Congratulations! You got it in 4 guesses.

from random import random

tries = 1
n = int(random()*99 + 1)

print "\nTime to play a guessing game.\n"
print "Enter a number between 1 and 100: ",
t = int(raw_input())

while t != n:
    if t > n: print "Too high. Try again: ",
    if t < n: print "Too low. Try again: ",
    t = int(raw_input())
    tries += 1

print "\nCongratulations! You got it in",tries,"guesses."
