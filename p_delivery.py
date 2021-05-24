# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978
from collections import deque

def solution(N, road, K):
    # dictionary로
    nodes = {}
    dist = {i:float('inf') if i != 1 else 0 for i in range(1,N+1)}

    for x,y,d in road:
        nodes[x] = nodes.get(x,[])+[(y,d)]
        nodes[y] = nodes.get(y,[])+[(x,d)]
    
    visited = deque([1])

    while visited:
        cur = visited.popleft()

        for nxt,d in nodes[cur] :
            
            if dist[nxt] > dist[cur]+d :
                dist[nxt] = dist[cur]+d
                visited.append(nxt)
        
        return len([True for dist in dist.values() if dist<=K])


    

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]] 
K = 3

print(solution(N,road,K))