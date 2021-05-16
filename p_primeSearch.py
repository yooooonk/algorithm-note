# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
import math

def isPrime(n) :
    if n<2 :
        return False
    q = math.sqrt(n)
    for i in range(2, int(q)+1) :
        if n%i == 0 :
            return False
    return True
        

def solution(numbers):
    numberList = list(numbers)
    answer = []

    # 모든 경우의 수
    for i in range(1,len(numbers)+1) :
        perlist = list(set(map(int,list(map(''.join,permutations(numberList,i))))))
        for p in perlist :   
            if(isPrime(p)):
                answer.append(p)   
    return len(set(answer))

print(solution('011'))    