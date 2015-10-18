#!/usr/bin/env python3
# Author: Narendra
# Usage: To find vowels
# logs: version 1.0 created on oct 17th

first_str=input("Please enter one character: ")

print(type(first_str))

if first_str == "a" or first_str == "e" or first_str == "i" or first_str == "o" or first_str == "u":
    print("Its a vowel.")
elif isinstance(first_str, str):
    print("Its a consonant.")
else:
    print("Its a number.")