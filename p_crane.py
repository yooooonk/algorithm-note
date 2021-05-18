# 인형뽑기
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
from collections import deque

# 내 풀이
""" def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    lane = [deque()*n for _ in range(n)]
    
    for i in range(n) :
        for j in range(n):
            doll = board[i][j]
            if doll>0 :
                lane[j].appendleft(doll)

    
    moveQ = deque(moves)
    while moveQ :        
        l = moveQ.popleft()-1
        if len(lane[l])>0 :
            doll = lane[l].pop()
            
            if len(stack)>0 and stack[-1]==doll:
                stack.pop()
                answer += 2
            else :
                stack.append(doll)    
    return answer """
# 개선    
def solution(board, moves):
    answer = 0
    stack = [0]
        
    for i in moves :
        for j in range(len(board)):
            doll = board[j][i-1]
            if doll>0 :
                board[j][i-1] = 0

                if stack[-1] == doll :
                    stack.pop()
                    answer += 2
                else :
                    stack.append(doll)
                break;
    return answer

board =  [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))