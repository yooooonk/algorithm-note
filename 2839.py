# 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys

input = sys.stdin.readline
n = int(input())

cnt = 0
while n>=0:
    if n %5==0:
        cnt += n//5
        print(cnt)
        break

    n -= 3
    cnt += 1

else :
    print(-1)

    # 3으로 나눴을 때 안나눠지면 -1 리턴