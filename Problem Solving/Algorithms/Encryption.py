#https://www.hackerrank.com/challenges/encryption/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    ss = ''.join(s.split())
    sqrt_len_ss = math.sqrt(len(ss))
    row = math.floor(sqrt_len_ss)
    col = math.ceil(sqrt_len_ss)
    if row * col < len(ss):
        row +=1
    enc = ''
    for c in range(col):
        for r in range(row):
            print((r*col + c))
            try:
                enc += ss[r*col + c]
            except:
                break
        enc += ' '
    return enc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
