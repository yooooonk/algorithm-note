# ATM
# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int,input().split()))
time.sort()

dp = []

total = time[0]
for i in range(1,len(time)) : 
                 
    time[i] = time[i]+time[i-1]
                
    total += time[i]

print(total)