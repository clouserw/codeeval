#! /bin/bash

# Given a decimal (base 10) number, print out its binary representation.
# https://www.codeeval.com/open_challenges/27/

while read line; do
    echo "obase=2;$line" | bc
done < $1
