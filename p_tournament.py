# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    mn = min(a,b)
    mx = max(a,b)
    answer = 0

    while True:
        answer += 1
        
        if mn%2 == 1 and mn+ 1 == mx:
            break; 

        mn = mn//2 + mn%2
        mx = mx//2 + mx%2
        
    return answer

print(solution(8,4,7))