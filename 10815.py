# 숫자카드
# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split())) # 갖고 있는 카드
# 이진 탐색을 사용하기 위해서 정렬
card.sort()

m = int(input())
judge_card = list(map(int,input().split()))

answer = []

def search(target,card) :
    min = 0
    max = n-1 #card 개수,idx이므로 -1

    while min<= max:
        mid = (min+max)//2

        if card[mid] == target:
            return 1
        elif card[mid] > target:
            # [x x x | x x x ] target이 mid보다 왼쪽이므로 max를 mid-1로
            max = mid-1
        else :
            # [x x x | x x x ] target이 mid보다 오른이므로 min min+1로
            min = mid+1
    # 검색할 카드가 없으면 while문이 다돌고 여기로 옴
    return 0

for i in judge_card :
    answer.append(search(i,card))

# 출력방식...
pp = " ".join(map(str,answer))
print(pp)