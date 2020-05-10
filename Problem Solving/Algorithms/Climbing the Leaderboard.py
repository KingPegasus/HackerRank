#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def bs(value, start, end, arr): #for desending array

    if end <= start: return start
    else:
        mid = ((end - start) // 2) + start
        if arr[mid] == value:
            if arr[mid-1] == value: # if equal, find lower ind
                return bs(value, start, mid, arr)
            else:
                return mid
        elif value < arr[mid]:
            return bs(value, mid+1, end, arr)
        elif value > arr[mid]:
            return bs(value, start, mid, arr)

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_pos = []
    s=0
    unique=0
    e = len(scores)

    for a in alice[::-1]:      
        ind = bs(value=a, start=s, end=e, arr=scores)
        unique += len(set(scores[s:ind]))
        s = unique+1
        alice_pos.append(s)
        if ind == 0 or ind == e:
            s= ind
        elif scores[ind] == scores[ind-1]:
            s= ind-1
        else:
            s= ind
        print('ind=',ind)
  
    return alice_pos[::-1]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
