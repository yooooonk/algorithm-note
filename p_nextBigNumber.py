# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def getBinarySum(quotient) :
    binarySum = 0
    while True :
            if quotient == 1 : 
                binarySum += 1
                break;
            m = quotient//2
            mod = quotient%2 
            binarySum += mod            
            quotient = m       
    return binarySum

def solution(n):
    # 이진수 변환 로직..
    answer = n   
    compare = getBinarySum(n)
       
    while True:
        answer += 1;
        if compare == getBinarySum(answer) :
            break;  
    

    return answer

print(solution(15))