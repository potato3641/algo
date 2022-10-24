dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
M, N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
coboard = set()
tomatoes = set()
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            coboard.add((i, j))
        if board[i][j] > -1:
            tomatoes.add((i, j))
if coboard == tomatoes:
    print(0)
else:
    newadds = set(coboard)
    while coboard != tomatoes:
        todo = True
        newtemps = set(newadds)
        newadds = set()
        for i, j in newtemps:
            for d in range(4):
                if (i+dy[d], j+dx[d]) in tomatoes and (i+dy[d], j+dx[d]) not in coboard and (i+dy[d], j+dx[d]) not in newadds:
                    newadds.add((i+dy[d], j+dx[d]))
                    todo = False
        coboard |= newadds
        if todo:
            cnt = -1
            break
        else:
            cnt += 1
    print(cnt)
