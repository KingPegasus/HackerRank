#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for num in range(i,j+1):
        temp = num
        digits = ''
        while temp != 0:
            digits += str(temp%10)
            temp = temp // 10
        num2 = int(digits)
        print(num, num2)
        if abs(num-num2)%k == 0:
            count += 1 
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
