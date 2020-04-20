#https://www.hackerrank.com/challenges/matrix-script/problem
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
lis = ['!','@','#','$','%','&',' ']
matrix = []
decode = ''
extra = ''
pre = False
first = False
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for j in range(n):
        try:
            elem = matrix[j][i]
            condition = elem in lis
            while(condition and first):
                extra += elem
                break
            while(condition and (not first)):
                decode += elem
                break
            while((not condition) and pre and first):
                decode+= ' '+matrix[j][i]
                extra = ''
                first = True
                break
            while((not condition) and pre and (not first)):
                decode+= matrix[j][i]
                extra = ''
                first = True
                break
            while((not condition) and (not pre)):
                decode+= matrix[j][i]
                extra = ''
                first = True
                break
            pre = condition
        except:
            pass
decode+=extra
print(decode)