# Copyright Pablo Varela, 2016
# From http://openbookproject.net/pybiblio/practice/wilson/leapyear.php
#
# Leap years occur according to the following formula:
# a leap year is divisible by four, but not by one hundred,
# unless it is divisible by four hundred.
# For example, 1992, 1996, and 2000 are leap years,
# but 1993 and 1900 are not. The next leap year that
# falls on a century will be 2400.
#
# Sample Session
#
# What year: 1999
# 1999 is not a leap year.
#
# What year: 1988
# 1988 is a leap year.

print "What year: ",
year = int(raw_input())

# keep in mind that year%400 returns 0 so 'not year%400' means that year IS divisible by 400
if not year%400: print year,"is a leap year."
elif not year%4 and year%100: print year,"is a leap year."
else: print year,"is not a leap year."
