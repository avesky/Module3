"""
Program: basic if-elif.py
Author: Andy Volesky
Last date modified: 09/13/2021

The purpose of this program:
Test making expressions.
Set MAX = 10, MIN = 0
Set a variable y to a value
Test whether y is above MAX
Test whether y is below MIN
Set a variable x to a value
Test whether it is between the MIN and MAX but does not equal MAX nor MIN
Test whether it is within MIN up to MAX but does not equal MAX
Test whether it is above MIN up to and including MAX
"""

MIN = 0
MAX = 10

#testing various values
y = 7

print(y > MAX) #expected False
print(y < MIN) #expected False

x = 0

print(MIN < x < MAX) #expcted False
print(MIN <= x < MAX) #expected True
print(MIN < x <= MAX) #expected False
