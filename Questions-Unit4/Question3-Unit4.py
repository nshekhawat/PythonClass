#!/usr/bin/env python
# Author: Narendra

__doc__ = '''
Create a list made up of all the following 4 lower-case words, 1 word per list item: ["the","dead","parrot","sketch"]
Assign this list to a reference called: parrot, Write and save (as for1.py ) a short program using a for loop, which
prints out each word in turn, with the first letter capitalised, together with the length of each word.

Your output should look like this:
The 3
Dead 4
Parrot 6
Sketch 6

Save a copy of this program as for2.py. Edit it so that each time you go through the list and print a word you print
one more uppercase letter than the previous word. Your output should look like this:
The
DEad
PARrot
SKETch
'''

parrot = ["the", "dead", "parrot", "sketch"]

for item in parrot:
    print "{} {}".format(item.capitalize(),len(item))

print "\n"

for i, item in enumerate(parrot):
    i += 1
    val = item[0:i].upper()
    print val + item[i::]
