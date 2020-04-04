#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist=list(arr)
    e = max(mylist)
    mylist2 = [x for x in mylist if x<e]
    print(max(mylist2))
