# 파도반 수열
# https://www.acmicpc.net/problem/9461

""" import sys
n = int(sys.stdin.readline())
numbers = []
dp = [0,1,1,1,2,2]

def getP(N):    
    last = len(dp)-1 
    if N > last:
        for t in range(last+1,N+1):
            dp.append(dp[t-1]+dp[t-5])
    print(dp[N])

for _ in range(n):
    numbers.append(int(input()))

for i in numbers :
    getP(i)

 """

import sys
n = int(sys.stdin.readline())
numbers = []
dp = [0,1,1,1]

for _ in range(n):
     numbers.append(int(input()))

def getP(n) :
    last = len(dp)-1
    if n>last:
        for i in range(last+1,n+1):
            dp.append(dp[i-2]+dp[i-3])
    print(dp[n])


for i in numbers :
    getP(i)