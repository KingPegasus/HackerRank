#https://www.hackerrank.com/challenges/find-angle/problem
from math import atan , degrees
AB = int(input())
BC = int(input())
Theta = degrees( atan(AB/BC) )
print( str(int(round(Theta,0))) + "°")
