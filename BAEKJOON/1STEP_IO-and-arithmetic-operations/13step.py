'''문제
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
'''

A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈
#sep 파라미터는 print 함수에서 출력할 값이 여러 개일 때 
# 각 값의 사이사이에 삽입할 문자를 지정할 수 있는 파라미터이다.