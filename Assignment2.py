#!/usr/bin/env python
# Author: Narendra
# Usage: Assignment 2

names = ['jhanvi','naresh','sunny','santo','jena','brahma','sri','brahma','sunny','naresh']
dup_names = []

for name in names:
    count = names.count(name)
    if count >= 2:
        dup_names += name.split()
        names.remove(name)

print "final list " + "=", names
print "duplicated " + "=", dup_names