#https://www.hackerrank.com/challenges/beautiful-triplets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    countTriplets = 0
    for i,a in enumerate(arr):
        temp = 0
        baseValue = a
        for b in arr[i+1:]:
            if b == baseValue+d:
                baseValue = b
                temp += 1
                if temp == 2:
                    countTriplets +=1
                    break
    return countTriplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
