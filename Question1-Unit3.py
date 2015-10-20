#!/usr/bin/env python
# Author: Narendra

'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

list_num = []

for num in range(1000, 3001):
    for n in str(num):
        if int(n) % 2 == 0:
            list_num.append(num)

print set(list_num)
