#https://www.hackerrank.com/challenges/migratory-birds/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    maxid = -1 
    maxcount = 0
    unique_arr = list(set(arr))

    for i,element in enumerate(unique_arr):
        count = arr.count(element)
        if count > maxcount:
            maxid = i
            maxcount = count
    
    return unique_arr[maxid]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
