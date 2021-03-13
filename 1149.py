# RGB거리
# https://www.acmicpc.net/problem/1149

""" 
R G B
- 1번 집 2번집 다른 색
- N번집은 N-1 집 색 같지 않아야한다
-  2<= i <= n-1    i-1 i i+1
"""

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int,input().split())))


for i in range(1,len(dp)) :
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+dp[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+dp[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0])+dp[i][2]

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))