# 바이러스
# https://www.acmicpc.net/problem/2606

import sys
n = int(sys.stdin.readline())
conn = int(sys.stdin.readline())

graph = []

for i in range(n+1):        
    graph.append([])

for i in range(conn):
    a,b = map(int,sys.stdin.readline().split())    
    graph[a].append(b) 
    graph[b].append(a) 

visited = []
stack = [1]

while stack :
    cur = stack.pop()    
    visited.append(cur)
    
    for i in graph[cur] :        
        if i not in visited:
            stack.append(i)

print(len(set(visited))-1)
        

    
    