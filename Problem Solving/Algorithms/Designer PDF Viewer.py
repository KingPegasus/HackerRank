#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxHeight = 0
    for letter in word:
        maxHeight = max( maxHeight, h[ord(letter)-97] )
    
    area = maxHeight * len(word)
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
