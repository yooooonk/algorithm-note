# 회전하는 큐
# https://www.acmicpc.net/problem/1021

""" 양방향 순환 큐!
- popleft
- rotate
 """

import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
place = list(map(int, sys.stdin.readline().split()))

cnt = 0
q = deque(range(len(place)))

for i in range(len(place)) :
    if place[i] == q[0]:
        q.popleft()
        continue
    index = q.index(place[i])

    if index > len(q)//2 :
        q.rotate(len(q)-i)
        cnt += (len(q)-i)
    elif index <= len(q)//2 :
        q.rotate(-index) #
        cnt += index
    q.popleft()

print(cnt)