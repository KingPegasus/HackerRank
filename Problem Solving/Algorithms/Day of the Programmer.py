#https://www.hackerrank.com/challenges/day-of-the-programmer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        day = 26
    elif year < 1918:
        if year%4 == 0:
            day = 12
        else:
            day = 13
    else:
        if year%400 == 0:
            day = 12
        elif year%4 ==0 and year%100!=0:
            day = 12
        else:
            day = 13
    out=  str(day) + '.09.' + str(year)
    return out
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
