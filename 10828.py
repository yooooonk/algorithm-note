# 스택
# https://www.acmicpc.net/problem/10828

n = int(input())
case =[]

for _ in range(n):
    case.append(list(input().split()))

stack = []

for c in case:
    f = c[0]    
    
    if f == 'push' :
        stack.append(c[1])        
    
    if f == 'top' :
        if len(stack):
            print(stack[-1])
        else :
            print(-1)                
    if f == 'size':
        print(len(stack))
    if f == 'pop':
        if len(stack):
            print(stack.pop())
        else :
            print(-1)                
    
    if f == 'empty':
        if stack :
            print(0)
        else :
            print(1)
            

        
    
