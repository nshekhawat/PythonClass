#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

list_num = []

for n in range(1000, 3001):
        if (int(n) / 1000) % 2 == 0:
            if ((int(n) % 1000) / 100) % 2 == 0:
                if (((int(n) % 1000) % 100) / 10) % 2 == 0:
                    if (((int(n) % 1000) % 100) % 10) % 2 == 0:
                        list_num.append(n)

print list_num
