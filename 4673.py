# 셀프넘버
dnList = []
def dn(n) : # 121
    
    acc = n
    for value in list(str(n)):        
        acc += int(value)
    return acc

for i in range(10000) : 
    
    n = i+1
    dnList.append(dn(n))
    
for i in range(10000) :
    n = i+1
    if not(n in dnList) :
        print(n) 

