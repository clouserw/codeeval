#! /usr/bin/python

# Given a string write a program to convert it into lowercase.
# https://www.codeeval.com/open_challenges/20/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./20.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            print line.lower(),

except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
