#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a program which can map() and filter() to make a list whose elements are square of even number in

[1,2,3,4,5,6,7,8,9,10].
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = map(lambda x: x**2, list1)

print filter(lambda y: y % 2 == 0, list2)
