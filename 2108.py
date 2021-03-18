# 통계학
# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

n = int(input()) 
num = []
for _ in range(n):
    num.append(int(input()))
num.sort()
def avg() :    
    print(int(round(sum(num)/n,0)))

def mid():
    mid = len(num)//2
    print(num[mid])

def mode():
    mode = {}
    for i in num:
        if i in mode.keys():
            mode[i] += 1
        else :
            mode[i] = 1
    
    max = min(mode.values())
    modeVal = []    
    for key in mode.keys() :
        if max < mode[key] :
            max = mode[key] 
            modeVal = [key]
        elif max == mode[key]:
            modeVal.append(key)
        
    modeVal.sort()    
    print(modeVal[1] if len(modeVal)>1 else modeVal[0])

def diff():
    print(max(num)-min(num))

avg()
mid()
mode()
diff()