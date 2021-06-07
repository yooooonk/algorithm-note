# 프로그래머스 lv2.짝지어제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
from collections import deque

def solution(s):
    
    # s를 배열로
    que = deque(s)
    
    # stack만들기
    stack = [que.popleft()]

    # 쌓으면서 비교
    while que :
        txt = que.popleft() 
        
        if len(stack) and stack[-1] == txt:
            stack.pop()
        else :
            stack.append(txt)
        
    # stack이 비었으면 1, 아니며 0
    
    return 0 if len(stack) else 1

s = 'cdcd'

print(solution(s))    