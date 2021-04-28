# fly me to te alpha centauri
# https://www.acmicpc.net/problem/1011

""" n = int(input())

def move(dist) :
    k = 0
    cnt = 0
    # k값 구하기
    # k(k+1)/2 + k(k-1)/2 = k*k
    while True:
        k+=1
        if k*k-dist >= 0 :
            break;
    # 정점찍고 내려오는 스텝이 거리와 같을 때 
    if dist - k*k == 0:
        cnt = k+k-1
    else: # 다른 경우는 정점에서 내려오면 dist를 넘어버리기 때문에 k-1을 해줌
        k = k-1 # k-1에서의 스텝은 dist보다 짧을 수 밖에 없음. dist까지의 거리에 따라 조건을 줌
        if dist-k*k<= k: # 거리가 k와 같거나 k보다 작으면 1스텝 추가
            cnt = k+k
        else :
            cnt = k+k+1  # 거리가 k보다 크다면 무조건 2k보다는 작음. 그럴 때 그 사이에 k^2과 (k+1)^2의 차이가 2k
    print(cnt)


for _ in range(n):
    x,y = map(int,input().split())
    move(y-x)    
"""

t = int(input())
for i in range(t) :
    x,y = map(int, input().split())
    diff = y-x

    if diff <= 3:
        print(diff)
    else:
        n = int(diff**0.5)
        if diff == n**2:
            print(2*n-1)
        elif n**2 < diff <= n**2 + n:
            print(2*n)
        else :
            print(2*n+1)