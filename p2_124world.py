"""
def solution(n):
    print('---------',n)
    dp = [0]*(n+1)
    
    dp[1] = '1'
    dp[2] = '2'
    dp[3] = '4'

    num = ['4','1','2']
    print('1'+'4')
    
    def getDp(i):  
        print(dp)      
        if dp[i]:
            print(dp[i])
            return dp[i]
        else :
            if i%3==0:
                dp[i] = getDp(n//3-1)+num[n%3]
            else:
                dp[i] = getDp(n//3)+num[n%3]
                print(dp[i])
            return dp[i]
        
    
    return getDp(n)
"""

# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        print(answer)
        n //= 3
    return answer


print(solution(14))