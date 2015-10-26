#!/usr/bin/env python
# Author: Narendra

'''WAP to find the min of the two numbers ?'''

num1 = int(raw_input("Enter first no.:"))
num2 = int(raw_input("Enter second no.:"))

if num1 < num2:
    print "%d is minimum" %(num1)
elif num1 == num2:
    print "Both numbers are equal."
else:
    print "%d is minimum" %(num2)
