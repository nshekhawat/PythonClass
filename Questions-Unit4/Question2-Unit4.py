#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Assign a list to a reference a , containing a regular sequence of 5 - 8 elements,
such that if you knew the first 3 elements you would be able to predict the rest. E.G: [3,6,9,12,15,21,24] .
- Using a slice operation assign 2 elements from the middle of your sequence: e.g. 12 and 15 to another list called c.
- Take a backup of your list a in b by assigning: b=a You might need to copy the backup in b back to a if you screw a up.
- Using the del operator twice on indexed elements of list a, remove the 2 elements from the middle of a that you
assigned into the list c. E.G if you had (blindly) used the above values your list might now look like: [3,6,9,18,21,24].
- Using a slice assignment operation, restore the list a to its original sequence by inserting list c into the
middle of list a.
'''
