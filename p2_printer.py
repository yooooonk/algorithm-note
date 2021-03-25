def solution(priorities, location):
    idx = []
    for i in range(len(priorities)) :
        idx.append(i)
    
    answer = 0

    while True:
        if priorities[0] >= max(priorities) and idx[0]==location :
            answer += 1        
            break;
        elif priorities[0] >= max(priorities):            
            priorities.pop(0)
            idx.pop(0)
            answer += 1        
        else :
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
    return answer
    

print(solution([1, 1, 9, 1, 1, 1],0))    