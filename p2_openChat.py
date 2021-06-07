# 오픈 채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    ment = {"Enter":"님이 들어왔습니다.","Leave":"님이 나갔습니다."}
    uid = {}
    # 1. id hash맵 만들기
    for r in record :
        rr = r.split(" ") 
        if rr[0] != 'Leave' :
            uid[rr[1]] = rr[2]
    
    # 2. answer 출력
    for r in record :
        rr = r.split(" ") 
        if rr[0] != 'Change' :
            answer.append(uid[rr[1]] + ment[rr[0]])
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))