# 좌표 정렬하기2

n = int(input())
array = []
for i in range(n) :  
    x,y = map(int,input().split())
    temp = [y,x]
    array.append(temp)

array.sort()
for i in array:
    print(i[1],i[0])