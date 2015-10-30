#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10 DIGITS 3
'''

input_var = input("Enter something: ")

int_count = 0
str_count = 0

for inputs in input_var:
    if inputs.isdigit():
        int_count += 1
    elif inputs.isalpha():
        str_count += 1

print "LETTERS {} DIGITS {}".format(str_count, int_count)
