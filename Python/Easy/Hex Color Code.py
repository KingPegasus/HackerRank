#https://www.hackerrank.com/challenges/hex-color-code/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for _ in range(N):
    line = input().strip()
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]', line, re.I)]
    for code in codes:
        print (code)
