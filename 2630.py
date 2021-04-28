# 색종이 만들기
# https://www.acmicpc.net/problem/2630

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))

white = 0
blue = 0
def cutPaper(x,y,n) :
    global white,blue
    color = paper[0][0]
    # 숫자체크
    flag = True
    for i in range(x,x+n) :   
        
        if not flag:
            break;     
        for j in range(y,y+n) :            
            
            if color != paper[i][j] :
                
                flag=False
                cutPaper(i,     j,     n//2)
                cutPaper(i,     j+n//2,n//2)
                cutPaper(i+n//2,j,     n//2)
                cutPaper(i+n//2,j+n//2,n//2) 
                break;         
    
    if flag:
        if color: # blue
            blue += 1            
        else :
            white += 1
            #print('흰색',white)
   
   
cutPaper(0,0,n)
print(white)
print(blue)