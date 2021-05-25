# 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    number = list(map(int,s.split(" ")))
    answer = "{} {}".format(min(number),max(number))
    return answer

s = "1 2 3 4"
print(solution(s))    