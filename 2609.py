# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

a,b = map(int,input().split())
GCD = 0
# 최대공약수
m,n = a,b
while True:
    c = a%b
    if c ==0:
        GCD = b
        print(b)
        break;
    a = b
    b = c

# 최소공배수 // 최대공약수 * 최소공배수 = ab
print(m*n//GCD)

    

