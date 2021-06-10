# 괄호변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

from collections import deque

def divide(p):
    right = 0
    left = 0
    
    u = ''

    p = list(p)
    
    while p :
        temp = p.pop(0)
        
        u += temp
        if temp == "(" :
            right += 1
        else :
            left += 1

        if right == left :
            break; 

    v = "".join(p)

    return u,v

def isCorrect(p) :
    #print('===isCorrect함수===',p)
    pp = deque(p)    
    stack = []
    while pp :
        n = pp.popleft()
        
    
        if len(stack) > 0  and n == ')' and stack[-1] == '(' :
            
            stack.pop()            
        else :
            stack.append(n)        
        

        #print('===stack===',stack)
    return len(stack) == 0



def solution(p) :
    #print('solution',p)
    
    answer = ''
    # 과정1
    if len(p) == 0 :
        return ''
    # 올바른 문자열 반환
    if isCorrect(p) :
       # print('isCorrect',p)
        return p
    
    # 과정2
    u,v = divide(p);
    
    #print('u',u,'v',v)
    
    if(isCorrect(u)) : # 과정3
        #print('correct',u)
        # 과정3-1
        answer += u+solution(v)
    else :# 과정4
        
        # 과정4-1
        answer += '('

        # 과정 4-2
        answer += solution(v)

        # 과정 4-3
        answer += ')'

        # 과정 4-4
        uu = u[1:len(u)-1]
        nu = ''
        #print('전',uu)
        for i in uu :
            if i == "(" :
                answer += ")"
            else :
                answer += "("
        #print('후',nu)
        

    return answer;

p = "(()())()"
print(solution(p))    

