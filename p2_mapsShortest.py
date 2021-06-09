# 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps) :
    move = [[0,1],[1,0],[-1,0],[0,-1]]

    r = len(maps)
    c = len(maps[0])

    table = [[-1 for _ in range(c)] for _ in range(r)]

    q = deque([[0,0]])

    table[0][0] = 1

    while q :
        y,x = q.popleft()

        for m in move :
            xx, yy = m
            
            ny = y + yy
            nx = x + xx

            if -1<ny<r and -1<nx<c :
                if maps[ny][nx] == 1:
                    if table[ny][nx] == -1 :
                        table[ny][nx] = table[y][x]+1
                        q.append([ny, nx])
            
    return table[-1][-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
