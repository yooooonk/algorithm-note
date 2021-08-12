# 회의실배정 https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())

time = []
# 빼기 시간순으로 정렬
for i in range(n) :
    time.append((list(map(int,input().split()))))

time.sort(key=lambda x:(x[1],x[0]))

cnt = 0
end = time[0][1]
# for t in time :
