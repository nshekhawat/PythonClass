#!/usr/bin/env python
# Author: Narendra
# Usage: Assignment 1
# logs: version 1.0 created on oct 18th

days = ['yesterday','today','tomorrow','dayafter','firstday']

for i, day in enumerate(days):
    i += 1
    val = day[0:i].upper()
    print val + day[i::]