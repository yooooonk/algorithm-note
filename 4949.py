# 균형잡힌 세상

""" 내가 틀린 이유

- pop을 할 때는 stack에 값이 있는지를 확인 
- stack[-1]로 마지막 값을 알 수 있음. 바로 뽑지말것..
- 아니면 pop해서 확인하고 안맞으면 다시 append하던지
- ( ([]) 이런 경우 flag는 바뀌지않았는데 false인 경우임
- stack이 비었는지도 확인해줘야함!!!
- () [] 여러쌍이므로 pop하고 바로 printㅎ면안됨 일단 끝까지 돌아야..
 

 """

while True:
    sentence = input()
    stack = []
    result = True
    if sentence == '.':
        break

    for i in sentence :
        if i == '(' or i == '[':
            stack.append(i)
            
        elif i == ')': # stack에 요소가 있는지 확인해줘야함     pop()       
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                result = False
                break
        elif i == ']' :
              if stack and stack[-1] == '[' :
                stack.pop()
              else :
                result = False
                break
    print('yes' if result and not(stack) else 'no')   