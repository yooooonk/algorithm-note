# 달팽이는 올라가고싶다
"""
구조화
- 입력 : 올라감A 미끄러짐B 정상V
- 자료구조?
- 패턴
- (낮에 A미터 올라감 - B미끄러짐) * n > V

내려오는 날 1을 빼주는게 포인트!!
"""
import sys
input = sys.stdin.readline

A,B,V = map(int,input().split())
# A*d - B(d-1) >= V
# Ad - Bd + B >= V
# d(A-B) >= V-B
# d >= (V-B)/(A-B)


x = (V-B)/(A-B);
print(int(x) if x== int(x) else int(x)+1)
