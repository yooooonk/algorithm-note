# 소수구하기
# 입력 받은 수의 배수를 빼보자
# 어떻게? 배열 여러번 순회? xN


a, b = map(int, input().split())

def isPrime(num) :
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
            return True

for i in range(a,b+1) :
    if isPrime(i):
        print(i)

""" def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)  """