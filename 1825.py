# 큐2
# https://www.acmicpc.net/problem/18258
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
case = []
for _ in range(n):
    case.append(list(input().split()))
    

for c in case:
    fn = c[0]
    if fn == 'push' :        
        q.append(c[1])
    
    elif fn == 'pop': 
        if q:
            print(q.popleft())
        else :
            print(-1)
    elif fn == 'size':
        print(len(q))
    
    elif fn == 'empty':
        if q :
            print(0)
        else :
            print(1)    
    elif fn == 'front':
        if q:
            print(q[0])
        else:
            print(-1)    
    elif fn == 'back':
        if q :
            print(q[-1])
        else :
            print(-1)


  
    