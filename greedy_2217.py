# [그리디] 2217. 로프
# https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))

# w = 개수 * 무게

arr.sort(reverse = True)
for i in range(n) :
     arr[i] = arr[i] * (i+1)
print(max(arr))
