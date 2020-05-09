#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
def # Enter your code here. Read input from STDIN. Print output to STDOUT
Eng_no = input()
Eng_list = input().split()
Fre_no = input()
Fre_list = input().split()

sysdiff = set(Eng_list) ^ set(Fre_list)
print(len(sysdiff))
