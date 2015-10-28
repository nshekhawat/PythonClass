#!/usr/bin/env python
# Author: Narendra

'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated
numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9
'''

num_list = raw_input("Enter num list separate by comma: ")

split_list = num_list.split(',')

output = [i for i in split_list if int(i) % 2 != 0]
sq_output = [int(i)**2 for i in split_list if int(i) % 2 != 0]


print ','.join(output)
print ','.join(str(x) for x in sq_output)