T = int(input())
for test_case in range(1, T + 1):
	N, M = map(int,input().split())
	board = []
	TOP = 0
	for i in range(N):
		line = list(map(int,input().split()))
		board.append(line)
	for i in range(N-M+1):
		for j in range(N-M+1):
			SUM = 0
			for k in range(M):
				for l in range(M):
					SUM += board[i+k][j+l]
			if (SUM>TOP):
				TOP = SUM
	
	
	
	
	
	
	
	
	
	print('#{} {}'.format(test_case,TOP))
