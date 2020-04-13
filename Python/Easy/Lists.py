#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    mylist = []
    for _ in range(N):
        in_list = input().split()
        if in_list[0][0] == 'i':
            mylist.insert(int(in_list[1]),int(in_list[2]))
        elif in_list[0][0] == 'p' and in_list[0][1] == 'r':
            print(mylist)
        elif in_list[0][0] == 'r' and in_list[0][2] == 'm':
            mylist.remove(int(in_list[1]))
        elif in_list[0][0] == 'a':
            mylist.append(int(in_list[1]))
        elif in_list[0][0] == 's':
            mylist.sort()
        elif in_list[0][0] == 'p' and in_list[0][1] == 'o':
            mylist.pop();
        elif in_list[0][0] == 'r' and in_list[0][2] == 'v':
            mylist.reverse()
