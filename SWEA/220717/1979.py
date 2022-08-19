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
	N, K = map(int, input().split())
	board = []
	for i in range(N):
		line = list(map(int,input().split()))
		board.append(line)
	rst = 0
	for i in range(N):
		checkerH = 0
		checkerV = 0
		for j in range(N):
			# Horizon
			if (board[i][j] == 1):
				checkerH += 1
				if (checkerH == K):
					if ( j == (N-1) ):
						checkerH = 0
						rst += 1
					elif ( board[i][j+1] == 0):
						checkerH = 0
						rst += 1
					else:
						checkerH += 1
			else:
				checkerH = 0
			# Vertical
			if (board[j][i] == 1):
				checkerV += 1
				if (checkerV == K):
					if ( j == (N-1) ):
						checkerV = 0
						rst += 1
					elif ( board[j+1][i] == 0):
						checkerV = 0
						rst += 1
					else:
						checkerV += 1
			else:
				checkerV = 0
	print('#{} {}'.format(test_case,rst))
	
	
	
	
