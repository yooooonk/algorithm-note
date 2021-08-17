# 그리디 -  회의실배정 https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())

time = []

for i in range(n) :
    time.append((list(map(int,input().split()))))

time.sort(key=lambda x:(x[1],x[0]))
cnt = 0
end = 0

for t in time :
    if t[0] >= end :
        cnt += 1
        end = t[1]

print(cnt)