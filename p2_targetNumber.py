# 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque
# BFS
def solution(numbers, target):
    answer = 0
    # q = deque()
    s = []
    s.append([numbers[0],0])
    s.append([-numbers[0],0])
    while s :
        
        temp,idx = s.pop()
        
        idx += 1

        if idx < len(numbers) :
            s.append([temp+numbers[idx],idx])
            s.append([temp-numbers[idx],idx])
        else :
            if temp == target :
                answer += 1               

    return answer

numbers = [1,1,1,1,1]
target = 3

print(solution(numbers,target))