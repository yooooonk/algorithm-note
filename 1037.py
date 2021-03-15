# 약수
# https://www.acmicpc.net/problem/1037

n = int(input())
divisor = list(map(int,input().split()))
divisor.sort()
if len(divisor) == 1:
    print(divisor[0]**2)
else :
    print(divisor[0]*divisor[-1])
