# 더하기 사이클

num = int(input())

n = num

cnt = int(0)

while True :
     ten = int(n/10)
     one = n%10
     total = ten+one
     n = int(str(n%10)+str(total%10))
     cnt += 1
     if(num == n):
          break

print(cnt)
    