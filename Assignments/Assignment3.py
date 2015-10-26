#!/usr/bin/env python
# Author: Narendra
# Usage: Assignment 3

students = ['jhanvi','naresh','sunny','santo','jena','brahma','sri']

for student in students:
    if student == 'sunny':
        for i in range(4,8,2):
            print "{0} result card".format(students[i])
        break
    print "{0} result card".format(student)