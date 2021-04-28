# 제로
# https://www.acmicpc.net/problem/10773

n = int(input())

number = []
for _ in range(n):
    i = int(input())
    if i == 0 :
        number.pop()
    else :
        number.append(i)

print(sum(number))