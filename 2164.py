# 카드2
# https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())
cards = list(range(1,n+1))
cards.reverse()
q = deque(cards)

while len(q)>1:
    q.pop()
    q.appendleft(q.pop())

print(q.pop())

