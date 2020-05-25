#https://www.hackerrank.com/challenges/kaprekar-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    found = False
    for num in range(p,q+1):
        temp = num**2
        digits = 0
        while temp > 0:
            temp = temp // 10
            digits += 1

        numSq = num**2
        l = digits // 2
        r = digits - l

        shift = len(str(bin(2**r)[2:]))
        leftNum = numSq // (10**r)
        rightNum = numSq - leftNum*(10**r)

        newNum = leftNum + rightNum
        if num == newNum:
            found = True
            print(num, end=' ')
    if found == False:
        print('INVALID RANGE')
            

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
