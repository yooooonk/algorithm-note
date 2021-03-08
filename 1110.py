# 더하기 사이클

num = int(input())

i = num

cnt = int(0)


while True :
     ten = int(i/10)   #2
     one = i%10   # 6
     total = ten+one   # 08
     
     i = int(str(one) + str(total%10)) 
     cnt += 1
     if(num == i) : 
          break

print(cnt)
