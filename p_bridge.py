
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = [0]*bridge_length    

    while onBridge:
        onBridge.pop(0)
        if len(truck_weights) > 0:   
                
            if sum(onBridge)+truck_weights[0] <= weight:
                
                onBridge.append(truck_weights.pop(0))
            else:                
                onBridge.append(0)
        answer += 1        

    
    return answer

print(solution(100,100,[10]))    