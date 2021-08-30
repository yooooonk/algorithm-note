# [그리디] 10162. 전자레인지
# https://www.acmicpc.net/problem/10162

import sys
input = sys.stdin.readline

n = int(input())

s = ''
button = [300,60,10]

if n%10 != 0:
    s = '-1'
else :
    for i in button:
        temp = n // i
        n = n % i
        s += str(temp) + ' '


print(s)