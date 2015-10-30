#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print
"No".
'''

input_str = raw_input("Enter a string: ")

if input_str in 'yesYESYes':
    print "Yes"
else:
    print "No"


