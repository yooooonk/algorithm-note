# 베트르랑 공준
# https://www.acmicpc.net/problem/4948

n_list = []
while True:
    n = int(input())    
    if n == 0:
        break;
    n_list.append(n)

def primeList(n) :
    chk = [True]*n
    m = int(n**0.5)

    for i in range(2,m+1):
        if chk[i] :
            for j in range(i*2,n,i):
                chk[j] = False
    return [i for i in range(2,n) if chk[i]]                

for n in n_list :    
    prime_list = list(primeList(n*2+1))
    idx=0
    
    
    for i in range(len(prime_list)) :
        if prime_list[i]> n :
            idx = i    
            break;    
    print(len(prime_list[idx:]))
    
    

