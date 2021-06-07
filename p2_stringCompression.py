# 프로그래머스 lv2. 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s) == 1:
        return 1
    result = []
    comp = ""
    # 1. 1부터 n//2까지 글자 짜르기
    for cut in range(1, len(s)//2+1) :
        count = 1
        compare = s[:cut]     
        
        # 2. cut만큼 잘라서 비교  
        for i in range(cut, len(s),cut):
            temp = s[i:i+cut]
            
            if compare == temp : # 같으면 cnt++
                count += 1
                
            else : # 다르면 문자열 만들고, 다음 글자 확인
                if count == 1:
                    count = ""
                
                comp += str(count)+compare
                
                compare = temp
                count = 1

        # 3. 마지막거 처리
        if count == 1:
            count = ""
        comp += str(count)+compare        
        result.append(len(comp))
        comp = ""
        
    return min(result)
        


s = "abcabcdede"
print(solution(s))    