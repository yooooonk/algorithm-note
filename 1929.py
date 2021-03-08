# 소수구하기
# 입력 받은 수의 배수를 빼보자
# 어떻게? 배열 여러번 순회? xN


m, n = map(int, input().split())

n+=1
prime = [True]*n
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(2*i,n,i):
            prime[j] = False

for i in range(m,n):
    if i >1 and prime[i] == True:
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

