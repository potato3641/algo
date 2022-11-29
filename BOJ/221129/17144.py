def miis(): return map(int,input().split())
def ii(): return int(input())
N, M, T = miis()
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
upClear = ()
downClear = ()
board = [list(miis()) for _ in range(N)]
coboard = set()
for i in range(N):
    for j in range(M):
        if board[i][j] == -1 and not upClear:
            upClear = (i, j)
            downClear = (i+1, j)
        if board[i][j] > 0:
            coboard.add((i, j))
def diffusion():
    nextDict = dict()
    for y, x in coboard:
        if board[y][x]:
            cnt = 0
            for d in range(4):
                if 0<=y+dy[d]<N and 0<=x+dx[d]<M and board[y+dy[d]][x+dx[d]]!=-1:
                    cnt += 1
                    if (y+dy[d], x+dx[d]) in nextDict:
                        nextDict[(y+dy[d], x+dx[d])] += board[y][x]//5
                    else:
                        nextDict[(y+dy[d], x+dx[d])] = board[y][x]//5
            if (y, x) in nextDict:
                nextDict[(y, x)] -= cnt*(board[y][x]//5)
            else:
                nextDict[(y, x)] = -cnt*(board[y][x]//5)
    return nextDict
def rotate_up():
    global board
    y, x = upClear
    # 순서 v < ^ >
    for i in range(y-2, -1, -1):
        board[i+1][x] = board[i][x]+0
    board[0] = board[0][1:] + [board[1][-1]]
    for i in range(1, y+1):
        board[i-1][M-1] = board[i][M-1]+0
    board[y] = [-1, 0] + board[y][1:-1]
def rotate_down():
    global board
    y, x = downClear
    # 순서 ^ < v >
    for i in range(y+2, N):
        board[i-1][x] = board[i][x]+0
    board[N-1] = board[N-1][1:] + [board[N-2][-1]]
    for i in range(N-3, y-1, -1):
        board[i+1][M-1] = board[i][M-1]+0
    board[y] = [-1, 0] + board[y][1:-1]
    
for _ in range(T):
    nextDict = diffusion()
    for y, x in nextDict:
        board[y][x] += nextDict[(y, x)]
    rotate_up()
    rotate_down()
    coboard = set()
    for i in range(N):
        for j in range(M):
            if board[i][j]>0:
                coboard.add((i, j))
print(sum(sum(x) for x in board)+2)
