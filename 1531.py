# Greedy - 1541. 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

arr = input().split('-')
s = 0

for i in arr[0].split('+'):
    s += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)
