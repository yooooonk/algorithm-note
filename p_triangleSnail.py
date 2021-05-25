def solution(n):
    answer = []
    
    # 이차원배열 만들기
    snail = [[0]*n for _ in range(n)]          
    num = 1
    x,y = -1,0

    for i in range(n) :
        for j in range(i,n) :
            print(i,j,num)            
                
            if i%3 == 0:
                x += 1

            elif i%3 == 1 :
                y += 1

            elif i%3 == 2 :
                x -= 1
                y -= 1
            
            snail[x][y] = num
            num += 1

    for i in snail :
        for j in i :
            if(j != 0) :
                answer.append(j) 
    
            
    return answer

print(solution(6))