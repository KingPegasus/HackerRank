#https://www.hackerrank.com/challenges/permutation-equation/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    arr = []
    for x in range(1,len(p)+1):
        ind = p.index(x) +1
        arr.append(p.index(ind)+1)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
