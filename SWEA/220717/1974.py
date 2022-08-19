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
	board = []
	flag = True
	for i in range(9):
		SUM = 0
		line = list(map(int,input().split()))
		dummy = {1,2,3,4,5,6,7,8,9}
		for i in range(9):
			dummy.discard(line[i])
		if (len(dummy)!=0):
			flag = False
#			if (test_case > 7):
#				print('horizen',end='')
#				print(' No.{}'.format(i),end='')
#				print(dummy)
#				print(line)
		board.append(line)
	if (flag):
		for j in range(9):
			dummy = {1,2,3,4,5,6,7,8,9}
			for i in range(9):
				dummy.discard(board[i][j])
			if (len(dummy)!=0):
				flag = False
#				if (test_case > 7):
#					print('vertical',end='')
#					print(' No.{}'.format(j),end='')
#					print(dummy)
				break
	if (flag):
		for j in range(3):
			if (flag == False):
				break
			for i in range(3):
				dummy = {1,2,3,4,5,6,7,8,9}
				for a in range(3):
					for b in range(3):
						dummy.discard(board[i*3+a][j*3+b])
				if (len(dummy)):
					flag = False
#					if (test_case > 7):
#						print('squre',end='')
#						print(' No.{}, No.{}'.format(i, j),end='')
#						print(dummy)
					break
	print('#{} '.format(test_case), end='')
	if (flag):
		print(1)
	else:
		print(0)
	
	
