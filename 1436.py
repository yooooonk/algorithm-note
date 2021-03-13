# 영화감독 숌
# https://www.acmicpc.net/problem/1436
# 부르탈포스 완전탐색 - 666이 들어간 모든 수를 탐색...

n = int(input())
answer = 666

while n :
    if '666' in str(answer):
        n -= 1    
    answer += 1

print(answer) # 맨 처음 666을 뺀다
    