str = input().upper()

codeList = {}

for s in str :    
    if(s in codeList) :        
        codeList[s] = codeList.get(s)+1
    else :
        codeList[s]=1
    
maxCnt = 0
key = 0
for s in codeList :
    v = codeList.get(s)
    if v == maxCnt :
        key = '?'
        break
    elif v > maxCnt :
        maxCnt = v
        key = s
print(key)
