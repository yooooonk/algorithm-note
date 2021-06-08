# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

# 시간초과
""" def solution(scoville, K):
    
    answer = 0

    while True:
                
        if min(scoville) >= K :
            break;
        elif len(scoville) == 1:
            answer = -1
            break;
        else :
            a = min(scoville)
            scoville.remove(a)
            b = min(scoville)
            scoville.remove(b)

            scoville.append(a+2*b)
            answer += 1            

    return answer """

import heapq

def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)

    while True:
                
        if scoville[0] >= K :
            break;
        elif len(scoville) == 1:
            answer = -1
            break;
        else :
            a = heapq.heappop(scoville)            
            b = heapq.heappop(scoville)                        

            scoville.append(a+2*b)
            answer += 1            

    return answer   



scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))