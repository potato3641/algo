# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	N, M = map(int,input().split())
	ai = list(map(int,input().split()))
	bj = list(map(int,input().split()))
	less_num = 0
	diff = 0
	zmr = list()
	flag = True
	if ( N>=M ):
		less_num = M
		diff = N-M
	else:
		less_num = N
		diff = M-N
		flag = False
	for cnt in range(0,diff+1):
		zm = 0
		for i in range(0,less_num):
			if (flag):
				zm += ai[i+cnt]*bj[i]
			else:
				zm += ai[i]*bj[i+cnt]
		zmr.append(zm)
		#less_num+=1
	zmr.sort()
	print('#{} {}'.format(test_case,zmr[diff]))
	
	
