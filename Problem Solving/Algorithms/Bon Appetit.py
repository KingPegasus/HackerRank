#https://www.hackerrank.com/challenges/bon-appetit/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = sum(bill)
    del(bill[k])
    charged = sum(bill)/2
    if charged == b:
        print('Bon Appetit')
    else:
        print(int(b- charged))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
