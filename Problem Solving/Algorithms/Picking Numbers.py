#https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    ss=0
    for i in a:
        b = [ x-i for x in a]
        t = [ (x<=1 and x>=0) for x in b]
        s = sum(t)
        if s > ss:
            ss=s
    return ss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
