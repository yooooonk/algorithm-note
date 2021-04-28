# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184

""" MAX = 21
dp = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]

def w(a,b,c):
    
    if a<=0 or b<=0 or c<=0 :
        return 1
    if a>20 or b>20 or c>20 :
        return w(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
 
    if a<b<c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
 
    dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

case = []
while True:
    a,b,c = map(int,input().split())    
    if (a,b,c) == (-1,-1,-1):
        break
    case.append([a,b,c])

for a,b,c in case :
    print("w(%d, %d, %d) = %d" % (a,b,c,w(a,b,c)))   
     """

max = 3
w = [[[0]*max for _ in range(max)] for _ in range(max)]

print(w)