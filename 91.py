#! /usr/bin/python

# Write a program which sorts numbers.
# https://www.codeeval.com/open_challenges/91/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./91.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = map(float, line.split())
            line.sort()
            print " ".join(map(lambda x: "{0:.3f}".format(x), line))
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
