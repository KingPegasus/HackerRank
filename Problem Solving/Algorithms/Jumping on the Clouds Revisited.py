#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    cost = 0
    n = len(c)
    i = k % n
    while i != 0:
        if c[i] == 1:
            cost += 3
        else:
            cost += 1
        i = (i+k)%n
    cost += 1 if c[i] == 0 else 3
    return 100 - cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
