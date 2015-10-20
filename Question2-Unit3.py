#!/usr/bin/env python
# Author: Narendra

'''
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100 W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100
Then, the output should be: 500
'''

transactions = raw_input("Please input transaction log: ")

transaction_log = transactions.split(' ')

for transaction in transactions:
    if transaction in "D" 