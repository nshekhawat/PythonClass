#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100 W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100
Then, the output should be: 500
'''

transactions = raw_input("Please input transaction log: ")

transaction_log = transactions.split(' ')

count = 0

for i, transaction in enumerate(transaction_log):
    if transaction == 'D':
        count += int(transaction_log[i+1])
    elif transaction == 'W':
        count -= int(transaction_log[i+1])

print count
