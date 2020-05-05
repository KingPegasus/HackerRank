#https://www.hackerrank.com/challenges/drawing-book/problem
#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if(n%2==0): #if even
        back_count = (n-p+1)//2
    else:
        back_count = (n-p)//2
    front_count = p//2
    return min(front_count,back_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
