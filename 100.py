#! /usr/bin/python

# Write a program which checks input numbers and determines whether a number is
# even or not.
# https://www.codeeval.com/open_challenges/100/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./100.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            if int(line) % 2:
                print 0
            else:
                print 1
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
