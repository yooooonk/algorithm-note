# 1010 다리 놓기
# https://www.acmicpc.net/problem/1010
# mCn = m!//(n! * (m-n)!)

n = int(input())
case = []

for i in range(n):
    case.append(list(map(int,input().split())))

def f(num):
    dp = [0]*(num+1)
    if num == 1 or num == 0:
        dp[num] = 1
        return dp[num]
    
    if dp[num]:        
        return dp[num]
    
    dp[num] = num*f(num-1)
    return dp[num]
   

for n,m in case:      
    print(f(m)//(f(n)*f(m-n))) 
