# 처음생각한거 - 오답
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