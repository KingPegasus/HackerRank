#https://www.hackerrank.com/challenges/acm-icpc-team/problem
#!/bin/python3

import math
import os
import random
import re
import sys
def combineAsNumber(string,string2):
    sameDigits = 0
    for (letter,letter2) in zip(string,string2):
        if (letter == '1') | (letter2 == '1'):
            sameDigits +=1
    return sameDigits


# Complete the acmTeam function below.
def acmTeam(topic):
    n = len(topic)
    maxSameDigits = -1
    maxsTeamCount = -1
    for i in range(0,n):
        for j in range(i+1,n):
            sameDigits = combineAsNumber(topic[i],topic[j])

            if sameDigits > maxSameDigits:
                maxSameDigits = sameDigits
                maxsTeamCount = 1

            elif sameDigits == maxSameDigits:
                maxsTeamCount += 1

            else:
                pass # ignore
            
    return maxSameDigits, maxsTeamCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
