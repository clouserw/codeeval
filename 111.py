#! /usr/bin/python

# In this challenge you need to find the longest word in a sentence. If the
# sentence has more than one word of the same length you should pick the first
# one.
# https://www.codeeval.com/open_challenges/111/

import sys

if not len(sys.argv) == 2:
    print "Usage: ./111.py <filename>"
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            words = line.split()
            words.sort(key=len, reverse=True)
            print words[0]
except:
    print "Unexpected error:", sys.exc_info()
    sys.exit(1)
