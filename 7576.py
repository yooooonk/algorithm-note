# 토마토
""" 
가로 m
세로 n개의 토마토상자
"""
import sys
from collections import deque
input = sys.stdin.readline

# 좌표이동
dx = [-1,1,0,0] # 위 아래
dy = [0,0,1,-1] # 우 좌


w,h = map(int,input().split())
tomato =[]
for _ in range(h):
    tomato.append(list(map(int,input().split())))

q = deque()
# 익은 토마토가 어딨나
for i in range(h):
    for j in range(w):
        if tomato[i][j] == 1:
            q.append([i,j])

# 토마토 전파
def bfs():
    global q
    while q:
        x,y = q.popleft()

        for i in range(4) : # 상하좌우
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < h and 0<=ny<w and tomato[nx][ny]==0:
                tomato[nx][ny] = tomato[x][y]+1
                q.append([nx,ny])

def go():
    ans = 0
    for i in range(h):
        for j in range(w):
            a=tomato[i][j]
            if a == 0:
                print(-1)
                return
            ans = max(ans,a)

    print(ans-1)

bfs()
go()