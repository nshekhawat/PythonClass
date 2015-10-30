#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
'''

input_data = raw_input("Enter comma separate numbers: ")

list1 = input_data.split(',')

print "{}{}".format(list1, tuple(list1))
