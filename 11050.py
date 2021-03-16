# 이항계수 1
# https://www.acmicpc.net/problem/11050
# 이항계수 nCk = n!/k!*(n-k)!
n,k = map(int, input().split())

dp = [0]*11

def factorial(num) :
    if num <= 1:
        dp[num] = 1
        return dp[num]
    
    if dp[num] != 0 :
        return dp[num]
    dp[num] = num*factorial(num-1)
    return dp[num]
        

print(factorial(n)//(factorial(k)*factorial(n-k)))
