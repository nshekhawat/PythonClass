#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the values only.
'''

def square(x):
    d = {}
    for i in range(1,x):
        d[i] = i**2
    return d.values()

if __name__ == "__main__":
    print square(21)

