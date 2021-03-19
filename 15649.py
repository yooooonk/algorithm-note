# N과 M
# https://www.acmicpc.net/problem/15649

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []
visited = [False]*n
def bt(cnt):
    global arr,n,m
    
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        
        if visited[i] == False :           
            visited[i] = True
            arr.append(i+1)
            bt(cnt+1)
            arr.pop()         
            visited[i] = False

bt(0)




