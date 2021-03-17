# DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
input = sys.stdin.readline

n,b,start = map(int,input().split())

graph = []
for i in range(n+1):        
    graph.append([])

for _ in range(b):
    i,j = map(int,input().split())

    graph[i].append(j)
    graph[j].append(i)

def DFS(start):    
    stack=[start]
    visited=[]
    while stack :
        cur = stack.pop()
        if cur not in visited:
            print(cur, end=' ')
        visited.append(cur)
        graph[cur].sort(reverse=True)
        for i in graph[cur]:
            if i not in visited:                
                stack.append(i)
   

def BFS(graph,start):    
    q=[start]
    visited=[]
    
    while q :
        cur = q.pop(0)        
        
        if cur not in visited: 
            print(cur, end=' ')
        visited.append(cur)    
        graph[cur].sort()
        #print(cur,end=' ')
        for i in graph[cur]:  
            #print('i',i,visited)          
            if i not in visited:
                q.append(i)
                
    

DFS(start)
print()
BFS(graph,start)


