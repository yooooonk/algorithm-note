# 최소공배수
# https://www.acmicpc.net/problem/1934

# 최대공약수*최대공배수 = a*b

n = int(input())
case = []

for _ in range(n):
    case.append(list(map(int,input().split())))


for a,b in case :
    GCD = 0
    m,n = a,b
        
    while True:
        c = m%n
        if c == 0:
            GCD = n
            break;
        m = n
        n = c
    print(a*b//GCD)


