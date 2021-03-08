# 소수구하기
# 입력 받은 수의 배수를 빼보자
# 어떻게? 배열 여러번 순회? xN

a,b = map(int,input().split())
fullArray = list(range(b+1))[a:]

def is_prime(i):
    if(i<=1) : return

    n=2
    while n*n <= i:
        if i%n == 0: return
        n+= 2
    print(i)

for i in fullArray :
    is_prime(i)
