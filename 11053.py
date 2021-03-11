# 가장 긴 증가하는 부분수열
# https://www.acmicpc.net/problem/11053

import sys
n = int(sys.stdin.readline())
answer = list(map(int,sys.stdin.readline().split()))

dp = [0]*n
for i in range(0, n):
    if i == 0 :
        dp[i] = 1
    else :
        max_dp = 0
        for j in range(0, i):
            if max_dp < dp[j] and arr[j] < arr[i]:
                max_dp = dp[j]
        dp[i] = max_dp+1

print(max(dp)) 

 

