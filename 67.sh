#! /bin/bash

# You will be given a hexadecimal (base 16) number. Convert it into decimal
# (base 10).
# https://www.codeeval.com/open_challenges/67/

while read line; do
    echo $((0x$line))
done < $1
