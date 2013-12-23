#! /usr/bin/python

# Write a program which swaps letters' case in a sentence. All non-letter
# characters should remain the same.
# https://www.codeeval.com/open_challenges/96/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./96.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            print line.rstrip().swapcase()
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
