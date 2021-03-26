# 기능개발
def solution(progresses, speeds):
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

