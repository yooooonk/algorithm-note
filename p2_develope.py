# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
""" def solution(progresses, speeds):
    answer = []
    
    while progresses: # 와일 한바퀴가 하루        
        
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        print(progresses)
        if progresses[0]>=100 :                
            while progresses:
                if progresses[0] < 100:
                    break;
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            answer.append(cnt)    
         
    return answer

print(solution([0, 0, 0, 0],[100, 50, 34, 25] 	))
 """
from collections import deque

def solution(pro, sp):
    progresses = deque(pro)
    speeds = deque(sp)
    answer = []
    while progresses :        
        
        # 작업량 계산
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 첫날거랑 비교 - 100넘으면 빼기
        cnt = 0
        if progresses[0] >= 100 :
            while progresses:
                if progresses[0] < 100:
                    break;
                speeds.popleft()
                progresses.popleft()
                cnt += 1
            print(cnt)
            answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))    