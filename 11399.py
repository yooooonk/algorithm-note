# ATM
# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input())
n2 = list(map(int, input().split()))

# 3 1 4 3 2

n2.sort()
print(n2)















n = int(input())
time = list(map(int,input().split()))
time.sort()

dp = []

total = time[0]
for i in range(1,len(time)) : 
                 
    time[i] = time[i]+time[i-1]
                
    total += time[i]

print(total)





