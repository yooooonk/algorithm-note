# 나무자르기
# 이진탐색이용
# while문을 빠져나오는 조건이 이해가 안감..
# 나무가 낮을때는 고려안함?

n,m = map(int,input().split())
trees = list(map(int,input().split()))

min = 0
max = max(trees)
tree = 0
answer = 0

while(min>=max):
    
    mid = (min+max)//2
    for i in trees :
        if mid > i :
            tree += i-mid
        
        if tree >= m:
            answer = mid
            min = mid+1
        else :
            max = mid-1


print(answer)
