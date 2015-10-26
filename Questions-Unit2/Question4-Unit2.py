#!/usr/bin/env python
# Author: Narendra

'''
Write a script which works out how old a child should be to know a certain word. The classification should be based
on the length of the word, as follows:
- 5 years <= 3 letters
- 6 years <= 4 letters
- 8 years <= 6 letters
- 10 years <= 10 letters
- 12 years = any length
'''

letter = raw_input("Please enter a letter: ")

if len(letter) <= 3:
    print "Child is 5 years old."
elif len(letter) <= 4:
    print "Child is 6 years old."
elif len(letter) <= 6:
    print "Child is 8 years old."
elif len(letter) <= 10:
    print "Child is 10 years old."
else:
    print "Child is 12 years old."