# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0,0]

    for i in range(1,len(words)) : 
        # 중복글자
        if words[i-1][-1] != words[i][0] or words.index(words[i]) < i :
            print(i)
            
            num = (i%n)+1
            cnt = (i+1)//n if (i+1)%n==0 else (i+1)//n+1
            answer = [num,cnt]                       
            break;

    return answer

n = 3
words = ["hello", "one", "even", "ggnever", "now", "world", "draw"]
print(solution(n,words))    