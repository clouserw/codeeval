#! /usr/bin/python

#  Having a string representation of a set of numbers you need to print this
#  numbers.  All numbers are separated by semicolon. There are up to 20 numbers
#  in one line.  The numbers are "zero" to "nine"
#
# https://www.codeeval.com/open_challenges/104/

from __future__ import print_function

import sys

if not len(sys.argv) == 2:
    print("Usage: ./104.py <filename>")
    sys.exit(1)

numbers = {'zero': 0,
           'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}

try:
    with open(sys.argv[1]) as f:
        for line in f:
            for num in line.split(';'):
                try:
                    print(numbers[num.strip()], end="")
                except:
                    pass
            print("")
except:
    pass
