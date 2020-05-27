#https://www.hackerrank.com/challenges/append-and-delete/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    sameIndex = -1
    #finding index from where difference starts
    for loc,(i,j) in enumerate(zip(s,t)):
        if i != j:
            break
        else:
            sameIndex = loc
    sameLength = sameIndex +1
    
    #length for processing
    length = len(s) + len(t) - (2 * sameLength)

    
    if length % 2 == 0 and k % 2 ==0 and k >= length:
        return 'Yes' 

    elif length % 2 == 1 and k % 2 == 1 and k >= length:
        return 'Yes'

    elif k >= sameLength * 2  and length == 0:
        return 'Yes'

    elif k >= len(s) + len(t):
        return 'Yes'

    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
