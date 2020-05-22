#https://www.hackerrank.com/challenges/taum-and-bday/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    totalCost = 0
    
    # If conversion cost less then the difference
    if z < abs(bc-wc): # Conversion can be useful
        minUnitCost = min(bc,wc) #min cost per item
        if bc < wc: # if black's cost is less
            blackCost = bc * b
            whiteCost = (bc * w) + (w * z) #buy black then convert
            totalCost = blackCost + whiteCost
        else:
            whiteCost = wc * w
            blackCost = (wc * b) + (b * z) #buy white then convert
            totalCost = blackCost + whiteCost

    else: #if not worth converting
        totalCost = (wc * w) + (bc * b)

    return totalCost 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
