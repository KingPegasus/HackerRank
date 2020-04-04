#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    Students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name,score]
        Students.append(student);

    min_score=100
    sec_min= 100
    for [a,b] in Students:
        if b < min_score:
            sec_min = min_score
            min_score = b
        elif b <sec_min and b> min_score:
            sec_min =b;
    
    mylist = [a for [a,b] in Students if b==sec_min]
    mylist = sorted(mylist)
    
    for x in mylist:
        print(x)
