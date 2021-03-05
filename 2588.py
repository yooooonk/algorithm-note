# 곱셈

"""
입력
472 385

출력
2360
3776
1416
181720  
"""
A = int(input()) 
B = input()      


list = B[::-1]

for n in list :
    print(A*int(n))
print(A*int(B))    

