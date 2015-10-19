#!/usr/bin/env python
# Author: Narendra
# Usage: Question 1 from Unit 1 exercises

'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-
separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: with-
out,hello,bag,world Then, the output should be: bag,hello,without,world'''

words_input = raw_input("Please enter comma separated input: ")

words = words_input.split(',')

words.sort()

print ",".join(words)

