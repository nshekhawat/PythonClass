#!/usr/bin/env python
# Author: Narendra

'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10 DIGITS 3
'''

input_var = input("Enter something: ")

first_input = input_var.split(' ')
int_count = 0
str_count = 0

for inputs in first_input:
    if isinstance(inputs, int) == True:
        int_count += 1
    elif isinstance(inputs, str) == True:
        str_count += 1

print "Numbers count: {}".format(int_count)
print "String count: {}".format(str_count)