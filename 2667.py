# 백준 2667. 단지번호 붙이기
# https://www.acmicpc.net/problem/2667

from collections import deque
import sys 
input = sys.stdin.readline

n = int(input())

apart = []

for _ in range(n) :
    apart.append(list(map(int,input().strip())))

table = [[-1 for _ in range(n)] for _ in range(n)]

move = [[1,0],[0,1],[-1,0],[0,-1]]

answer = []
for y in range(n) :
    for x in range(n):
        
        if apart[y][x] == 1 and table[y][x] == -1:
            cnt = 1
            visited = deque()

            visited.append([y,x])
            table[y][x] = cnt
            
            while visited :
                vy, vx = visited.popleft()                
                
                for m in move :
                    ny = vy+m[0]
                    nx = vx+m[1]

                    if -1 < ny < n and -1<nx<n :
                        if apart[ny][nx] == 1 and table[ny][nx] == -1:
                            
                            cnt += 1
                            table[ny][nx] = cnt
                            visited.append([ny,nx])                            
            answer.append(cnt)

answer.sort()
print(len(answer)) 
for i in answer :
    print(i)