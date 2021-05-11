# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def getDivisor(n) : 
    divisor = []
    
    for i in range(1, int(n**0.5)+1):
        
        if(n%i == 0) :            
            if(i != (n//i)) :
                divisor.append([i,n//i])
            else :
                divisor.append([i,i])
            
    return divisor
    

def solution(brown, yellow):
    answer = []
    pair = getDivisor(yellow)

    for i in pair :
        a,b = i
        carpet = 2*(a+b)+4

        if carpet == brown :
            answer.append(b+2)
            answer.append(a+2)
            break; 
    
    return answer

"""
def solution(brown, yellow) :
    answer = []
    
    for i in range(1, int(yellow**0.5)+1) :
        if yellow % i == 0 :
            if 2*(i+yellow//i)+4 == brown :
                return [yellow//i+2, i+2]
"""   

print(solution(24,24))