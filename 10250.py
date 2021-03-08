# ACM 호텔
""" 
- w로 만든 배열
- 사람수/h = w
- 나머지 = 호수?

## 나머지가 0일 때의 처리, 표현
"""

case = int(input())

for i in range(case):    
    h,w,n = map(int,input().split())
    room = n//h+1
    floor = n%h
    if floor == 0:
        room -= 1
        floor = h
    print(f'{floor*100+room}')
