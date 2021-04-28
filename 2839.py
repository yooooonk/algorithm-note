# 설탕 배달
# https://www.acmicpc.net/problem/2839

""" n = int(input())
pack = 0

while True:
    if n%5==0:
        pack += n//5
        print(pack)
        break;

    n -= 3
    pack += 1

    if n<0 :
        print(-1)
        break;
 """
sugar = int(input())

pack = 0
while True:
    
    if sugar%5 ==0:
        pack += sugar//5
        break;    
    sugar -= 3
    pack += 1

    if sugar < 0 :        
        pack = -1
        break;    

print(pack)
    


