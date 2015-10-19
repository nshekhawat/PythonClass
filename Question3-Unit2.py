#!/usr/bin/env python3
# Author: Narendra
# Usage: To find vowels

first_str=input("Please enter one character: ")

if first_str in 'aeiou':
    print("Its a vowel.")
elif isinstance(first_str, str):
    print("Its a consonant.")
else:
    print("Its a number.")
