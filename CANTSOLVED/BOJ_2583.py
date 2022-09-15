N, M, K = map(int,input().split())
coboard = [list(map(int,input().split())) for _ in range(K)]
board = [['a']*M for _ in range(N)]
for sc, sr, ec, er in coboard:
    for r in range(sr, er):
        for c in range(sc, ec):
            board[r][c] = 0
cntarray = []
cnt = 1
for i in range(N):
    for j in range(M):
        if board[i][j]: # 비어있다면
            todo = True
            if i > 0 and type(board[i-1][j])==type(['a']):
                if type(board[i][j])==type('a'):
                    board[i][j] = board[i-1][j]
                else:
                    board[i][j][0] = board[i-1][j][0]
                todo = False
            if j > 0 and type(board[i][j-1])==type(['a']):
                if type(board[i][j])==type('a'):
                    board[i][j] = board[i][j-1]
                else:
                    board[i][j][0] = board[i][j-1][0]
                todo = False
            if todo:
                cntarray.append([str(cnt)])
                board[i][j] = cntarray[-1]
                cnt += 1
rst = [0]*(cnt+1)
for c in range(1,cnt+1):
    for i in range(N):
        rst[c] += board[i].count([str(c)])
rst = [x for x in rst if x!=0]
rst.sort()
print(len(rst))
print(*rst)
