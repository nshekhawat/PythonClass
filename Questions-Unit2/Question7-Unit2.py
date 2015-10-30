#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Write a small password checking script. This will record the username, old password and new password.
The rules are that a password is OK if it is >7 characters long, contains some uppercase characters and
is different to the old password. The admin user (username 'admin') can do whatever they like.
Print out whether the new password is OK.
'''

username = raw_input("Enter a username: ")
old_passwd = raw_input("Enter old password: ")
new_passwd = raw_input("Enter new password: ")

if len(new_passwd) >=7 and any(passwd in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for passwd in new_passwd) and new_passwd != old_passwd:
    print "New password is OK."
else:
    print "New password is not OK."