#!/usr/bin/env python
# Author: Narendra
# Usage: Question 3 from Unit 1 exercises

__doc__ = '''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello
world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect
practice world'''

whitespaceline_input = raw_input("Enter whitespace separated line: ")

lines = whitespaceline_input.split(' ')

for line in lines:
    count = lines.count(line)
    if count >= 2:
        lines.remove(line)

lines.sort()
final = ' '.join(lines)
print final

