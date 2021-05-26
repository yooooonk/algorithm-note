# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978
from collections import deque

def solution(N, road, K):
    graph = {}
    dist = {i:float('inf') if i != 1 else 0 for i in range(1, N+1) }
    
    for v1, v2, d in road:
        graph[v1] = graph.get(v1, []) + [(v2, d)]
        graph[v2] = graph.get(v2, []) + [(v1, d)]
    visited = deque([1])
    
    while visited:
        cur_node = visited.popleft()
        for nxt_node, d in graph[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d:
                dist[nxt_node] = dist[cur_node] + d
                visited.append(nxt_node)

    return len([True for dist in dist.values() if dist <= K])
    

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]] 
K = 3

print(solution(N,road,K))