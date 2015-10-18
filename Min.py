#!/usr/bin/env python
# Author: Narendra
# Usage: To find min of two numbers
# logs: version 1.0 created on oct 17th

num1 = int(raw_input("Enter first no.:"))
num2 = int(raw_input("Enter second no.:"))

if num1 < num2:
    print "%d is minimum" %(num1)
elif num1 == num2:
    print "Both numbers are equal."
else:
    print "%d is minimum" %(num2)
