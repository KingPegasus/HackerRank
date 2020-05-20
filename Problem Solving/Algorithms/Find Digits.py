#https://www.hackerrank.com/challenges/find-digits/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp = n
    count = 0
    while(temp >0):
        if temp%10 !=0:
            if (n % (temp%10)) ==0 :
                count += 1
        temp = temp//10
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
