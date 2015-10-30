#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
write a program which takes 2 digits , X,Y as input and generates a 2 dimensional array.
The element value in the i-th row and j-th column of the array is i*j Note: i=0,1..., X-1; j=0,1,iY-1
Example: Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be: [[0,0,0,0,0]],[0,1,2,3,4],[0,2,4,6,8]]
'''

X = int(raw_input("Enter first digit X: "))
Y = int(raw_input("Enter second digit Y: "))

list1 = []

for i in range(0, X):
    list1.append([])
    for j in range(0, Y):
        list1[i].append(i*j)

print list1
