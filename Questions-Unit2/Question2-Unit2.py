#!/usr/bin/env python
# Author: Narendra

__doc__ = '''Wap to find the max of the three numbers ?'''

num1 = int(raw_input("Enter first no.:"))
num2 = int(raw_input("Enter second no.:"))

if num1 > num2:
    print "{} is maximum".format(num1)
elif num1 == num2:
    print "Both numbers are equal."
else:
    print "{} is minimum".format(num2)
