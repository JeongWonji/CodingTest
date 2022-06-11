'''문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
'''

A,B = input().split()
A = int(A)
B = int(B)
print(A+B)	
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)

#a에서 b를 나눈 값을 출력하는 코드인데, 코드 작성의 차이. 
# 파이썬의 경우 정수 둘을 나누고 떨어지지 않을 때 자동으로 
# float형으로 출력하여 준다. 
# 하지만 예제 출력을 보면 둘을 나눴을 때도 int 형으로 
# 출력하여야 하기에 int(A/B)해줌

A, B = input().split()
A = int(A)
B = int(B)
print(A+B)   
print(A-B)
print(A*B)
print(A//B)
print(A%B)