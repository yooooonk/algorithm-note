# 숫자카드
# https://www.acmicpc.net/problem/10815
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
sorted_card = sorted(card)

m = int(input())
judge_card = list(map(int,input().split()))
answer=[]

def search(target,card):    
    min = 0
    max = n-1    
        
    while min <= max:        
        mid = (min+max)//2
                 
        if card[mid] == target:
            return 1            
        elif card[mid] > target :
            max = mid-1
        else :
            min = mid+1        
    return 0

for i in judge_card :    
    answer.append(search(i,sorted_card))

pp = " ".join(map(str, answer))
print(pp)