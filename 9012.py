# 괄호
# https://www.acmicpc.net/problem/9012

n = int(input())
case = []
for _ in range(n):
    case.append(input())


def isVPS(str) :
    s2 = []
    s1 = list(str)
    flag = True
    for s in s1:        
        if s == '(':            
            s2.append(s)
        
        if s == ')' :            
            if len(s2) and s2[-1] == '(':
                s2.pop()
            else :
                flag = False
                break;
            
    if flag and len(s2) == 0 :
        print('YES')
    else :
        print('NO')


for c in case:    
    isVPS(c)

