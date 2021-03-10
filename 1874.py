m = int(input())

stack = []
result = []
cnt = 1
bool = True

for n in range(m) :
    a = int(input())
    while cnt <= a : # 숫자를 일단 쌓은다음!
        stack.append(cnt)
        result.append('+')
        cnt += 1    
    if stack[-1] == a :
        stack.pop()            
        result.append('-')            
    else :            
        bool = False
        break;
        
if bool :
    for i in result:
        print(i)
else :
    print('NO')