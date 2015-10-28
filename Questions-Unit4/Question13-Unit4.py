#!/usr/bin/env python
# Author: Narendra

'''
With a given tuple (1,2,3,4,5,6,7,8,9,10),
write a program to print the first half values in one line and the last half values in one line.
'''

tuple1 = (1,2,3,4,5,6,7,8,9,10)

middle = len(tuple1) / 2

print tuple1[:middle]
print tuple1[middle:]