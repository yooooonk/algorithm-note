# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

""" 
n = int(input())
word = []

for _ in range(n):
    word.append(input())

cnt = 0
for w in word :
    forward = [0]
    flag = True
    for a in w:
        if a not in forward:
            forward.append(a)
        elif a == forward[-1]:            
            forward.append(a)
        else:
            flag = False
    
    if flag :
        cnt += 1    

print(cnt)
        

 """

n = int(input())
cnt = 0
for _ in range(n):    
    word = input()
    
    flag = True
    forward = []
    for s in word :        
        if s not in forward :
            forward.append(s)
        elif s == forward[-1] :
            forward.append(s)
        else :
            flag = False
            break
    
    if flag :
        cnt += 1

print(cnt)        
            

