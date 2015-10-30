#!/usr/bin/env python
# Author: Narendra

'''
Write a program to generate and print another tuple whose values are even numbers in the given tuple

(1,2,3,4,5,6,7,8,9,10).
'''

tuple1 = ()
tuple2 = ()

for i in range(1, 11):
    tuple1 += (i,)

for j in tuple1:
    if j % 2 == 0:
        tuple2 += (j,)

print tuple1
print tuple2

