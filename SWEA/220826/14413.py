T = int(input())
for tc in range(1, T+1):
	N, M = map(int,input().split())
	line = [list(input()) for _ in range(N)]
	flag_black = -1
	flag_white = -1
	rst = False
	for i in range(N):
		for j in range(M):
			if line[i][j] == '#':
				flag_black = i+j
				break
			if line[i][j] == '.':
				flag_white = i+j
				break
		if flag_black != -1 or flag_white != -1:
			break
	else:
		rst = True
	flag = False
	for i in range(N):
		for j in range(M):
			if flag_black != -1:
				if flag_black%2 == (i+j)%2:
					if line[i][j] == '.':
						flag = True
						break
				else:
					if line[i][j] == '#':
						flag = True
						break
			if flag_white != -1:
				if flag_white%2 == (i+j)%2:
					if line[i][j] == '#':
						flag = True
						break
				else:
					if line[i][j] == '.':
						flag = True
						break
		if flag:
			break
	else:
		rst = True
	print(f'#{tc}', 'possible' if rst else 'impossible')