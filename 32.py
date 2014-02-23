#! /usr/bin/python

# You are given two strings 'A' and 'B'. Print out a 1 if string 'B' occurs at
# the end of string 'A'. Else a zero.
#
# https://www.codeeval.com/open_challenges/32/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./32.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            a, b = line.split(',')
            if a.endswith(b.strip()):
                print 1
            else:
                print 0
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
