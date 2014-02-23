#! /usr/bin/python

# Write a program which capitalizes the first letter of each word in a sentence.
#
# https://www.codeeval.com/open_challenges/93/

import sys
import string

if not len(sys.argv) == 2:
    print "Usage: ./93.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for l in f:
            # Can't use built-ins like title() here because it lowercases all
            # letters but the first
            print ' '.join(x[0].upper() + x[1:].rstrip() for x in l.split(' '))
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
