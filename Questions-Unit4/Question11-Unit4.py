#!/usr/bin/env python
# Author: Narendra

'''
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys.
'''
def square(x):
    d = {}
    for i in range(1,x):
        d[i] = i**2
    return d

if __name__ == "__main__":
    print square(21)

