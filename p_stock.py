# 프로그래머스 - 주식가격  
# https://programmers.co.kr/learn/courses/30/lessons/42584
# 문제 이해 잘못함. 주식을 유지하는 기간!
from collections import deque

def solution(prices):
    answer = []

    q = deque(prices)

    while q :
        p = q.popleft()
        s = 0;

        for i in q :
            s += 1
            if p > i : 
                break;
                        
        answer.append(s)
    
    return answer

print(solution([1, 2, 3, 2, 3]))    