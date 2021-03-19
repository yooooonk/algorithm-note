# 수 찾기
# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline
case = []
for _ in range(4):
    case.append(list(map(int,input().split())))

n = case[0][0]
nList = case[1]
m = case[2][0]
mList = case[3]

for mm in mList:
    if mm in nList:
        print(1)
    else:
        print(0)