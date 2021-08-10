# 회의실배정 https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())

time = []

for i in range(n) :
    temp = list(map(int,input().split()))
    temp.append(temp[1]-temp[0])
    time.append(temp)


print(time)