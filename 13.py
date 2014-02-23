#! /usr/bin/python

# Write a program to remove specific characters from a string.
#
# https://www.codeeval.com/open_challenges/13/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./13.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            a, b = line.split(',')
            print a.translate(None, b.strip())
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
