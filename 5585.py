import sys

input = sys.stdin.readline
n = 1000-int(input())
unit = [500,100,50,10, 5,1]

c = 0
for u in unit :

    c += n//u
    n = n%u


print(c)
