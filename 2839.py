# 설탕 배달
# https://www.acmicpc.net/problem/2839

n = int(input())
pack = 0

while True:
    if n%5==0:
        pack += n//5
        print(pack)
        break;

    n -= 3
    pack += 1

    if n<0 :
        print(-1)
        break;

""" 
내 원래답 

pack += n//5 # 6인 경우 여기서 걸려버림
pack += n%5//3

if n%5%3 != 0  d
 print(-1)
"""