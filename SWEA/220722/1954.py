T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case} ')
    N = int(input())
    cnt = 1
    rowval = [0, 1, 0, -1]
    rowidx = 0
    colval = [1, 0, -1, 0]
    colidx = 0
    i = 0
    j = 0
    lines = [[0]*(N+1) for _ in range(N+1)]
    for k in range(N+1):
        lines[N][k] = 9999
        lines[k][N] = 9999
    while True:
        if N == 1:
            lines[0][0] = 1
            break
        if N == 2:
            lines[0][0] = 1
            lines[0][1] = 2
            lines[1][0] = 4
            lines[1][1] = 3
            break
        lines[i][j] = cnt
        if lines[N//2][N//2 if N%2==1 else N//2-1] > 0:
            break
        if rowval[rowidx] != 0 and lines[i+rowval[rowidx]][j] > 0:
	        rowidx += 1
	        rowidx %= 4
	        colidx += 1
	        colidx %= 4
        if colval[colidx] != 0 and lines[i][j+colval[colidx]] > 0:
	        rowidx += 1
	        rowidx %= 4
	        colidx += 1
	        colidx %= 4
        i += rowval[rowidx]
        j += colval[colidx]
        cnt += 1
    for i in range(N):
        for j in range(N):
            print(f'{lines[i][j]}',end=' ')
        print()
