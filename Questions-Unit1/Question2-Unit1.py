#!/usr/bin/env python
# Author: Narendra
# Usage: Question 2 from Unit 1 exercises

__doc__ = '''Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the
output should be: HELLO WORLD PRACTICE MAKES PERFECT'''

line_input = raw_input("Enter a line: ")

print line_input.upper()
