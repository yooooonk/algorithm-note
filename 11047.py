# 동전0
# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coinList = []
for _ in range(n) :
    coinList.append(int(input()))

coinList.sort(reverse=True)
coin = 0
for c in coinList :    
    print(c)
    coin += k//c        
    k = k%c
print(coin)        