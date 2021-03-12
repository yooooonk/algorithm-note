# 수 정렬하기2
# https://www.acmicpc.net/problem/2751

import sys 
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))

""" def merge_sort(arr):
    n = len(arr)
    if n<= 1:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    while left and right :
        if left[0] < right[0]:
            result.append(left.pop(0))
        else :
            result.append(right.pop(0))
    while left :
        result.append(left.pop(0))
    while right :
        result.append(right.pop(0))

    return result


for i in merge_sort(arr) :
    print(i)   """   

""" 
메모리 205360kb / 852ms
"""
arr.sort()
for i in arr :
    print(i) 


