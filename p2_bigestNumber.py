# 정렬 - 가장 큰수
# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers) :
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3,reverse=True)
    print(numbers)
    return "0"

numbers =[3, 30, 34, 5, 9]

print(solution(numbers))