
"""
# 받는 방법
# # 속도 빠르게 받기
import sys 
input = sys.stdin.readline  # 한 라인 받는 함수 -- 결과적으로 input()처럼 사용하면 됨

# 한개만 받기
n = input() # input은 기본적으로 string으로 들어옴. 
m = int(input()) # string을 정수형태로 바꿔줘서 연산이 가능해짐

# 여러개 받기
# 입력값 : 10 20 30  
a,b,c = input().split() # split은 공백을 기준으로 자르는 함수. 10/20/30 각각 a='10',b='20', c='30'으로 들어옴
numberList = input.split() # [10,20,30] list 형태로 받음

# 여러개 받고 + 형변환
a,b,c = map(int,input().split()) # input().split()으로 받은 값을 int형으로 바꿔서 각각 a=10,b=20,c=30으로 받음
numberList = list(map(int,input().split())) # [10,20,30]리스트 형식으로 받음. map을 list로 감싸주는 이유는 map 객체는 print하면 주소값만 나오기 때문에 사용하기 편하게 하려고.

ex]
4 
1 2
1 3
1 4
2 4
"""
import sys 
input = sys.stdin.readline

n = int(input())

# 각각 받기 - 한번에 받기 부분 주석처리하고 실행
""" for _ in range(n):    
    a,b = input().split()    # 스트링    
    print('바로출력',a,b) 

    a,b = map(int,input().split())    # int
    print('바로출력',a,b)     
"""

# 한번에 받기 - 각각 받기 부분 주석처리하고 실행
case = []
for _ in range(n):    
    #nList = input().split()    # 스트링
    #nList = map(int,input().split()) # int 주소 나옴
    nList = list(map(int,input().split())) # list로 나옴
    case.append(nList)

print('한번에 출력',case)

# case 리스트를 만들었을 때 함수 이용은 for문으로 돌리면됨
for i in case :
    # 처리할 로직
    print(i)