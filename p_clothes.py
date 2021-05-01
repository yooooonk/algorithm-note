# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    # 경우의 수 : 각 1개일 때 = 전체 더하기
    case = {}
    answer = 1
    for ele in clothes :
        key = ele[1]
        if(key in case.keys()) :
            case[key] += 1
        else :
            case[key] = 1
    # 경우의 수 answer *= (옷 가지수+안 입을 경우) - 1(모두다 안입는 경우)
    for c in case.values():
        answer *= (c+1)

    return answer-1
    

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))    