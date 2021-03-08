# 4344 평균은 넘겠지

num = int(input())
jumsuList = []
# 입력값 받기
for i in range(num) :    
    line = list(map(int, input().split()))
    jumsuList.append(line)

for line in jumsuList :        
    avg = sum(line[1:])/line[0]
    cnt = 0
    for score in line[1:]:
        if score > avg :
            cnt += 1
    rate = cnt/line[0]*100
    print(f'{rate:.3f}%')


#for i in range(case) :
