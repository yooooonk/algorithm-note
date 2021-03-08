# 달팽이는 올라가고싶다
"""
구조화
- 입력 : 올라감A 미끄러짐B 정상V
- 자료구조?
- 패턴
- (낮에 A미터 올라감 - B미끄러짐) * n > V

내려오는 날 1을 빼주는게 포인트!!
"""

#  시간초과
""" 
cur = 0
day = 0
while True :
    cur += up    
    day += 1 # 하루  
    if(cur>=top) : break;    
    cur -= down    
print(day)     
"""
# up*x - down*(x-1) >= top  
# x >= (top-down)/(up-down)

up,down,top = map(int,input().split())
x = (top-down)/(up-down)
print(int(x) if x == int(x) else int(x)+1)


#print(int(day) if int(day)==day else int(day)+1)    


