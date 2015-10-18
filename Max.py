#!/usr/bin/env python
# Author: Narendra
# Usage: To find max of two numbers
# logs: version 1.0 created on oct 17th

num1 = int(raw_input("Enter first no.:"))
num2 = int(raw_input("Enter second no.:"))

if num1 > num2:
    print "%d is maximum" %(num1)
elif num1 == num2:
    print "Both numbers are equal."
else:
    print "%d is maximum" %(num2)