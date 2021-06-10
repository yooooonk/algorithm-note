# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):


    phone_book.sort()

    for i in range(len(phone_book)-1) :
        
        if(phone_book[i+1].find(phone_book[i]) == 0) :
            return False;
    return True
    

    



phone_book = ["12","123","1235","567","88"]

print(solution(phone_book))