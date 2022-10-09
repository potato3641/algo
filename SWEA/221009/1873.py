def miis(): return map(int,input().split())
def ii(): return int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
diridx = ['^', 'v', '<', '>']
orderidx = 'UDLRS'

T = ii()
for tc in range(1, T+1):
    N, M = miis()
    board = [list(input()) for _ in range(N)]
    ordercnt = ii()
    orders = list(input())
    tankco = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] in diridx:
                tankco = (i, j)
    for order in orders:
        now = orderidx.index(order)
        y, x = tankco
        if now == 4: # shoot
            d = diridx.index(board[y][x])
            cnt = 1
            while 0<=y+dy[d]*cnt<N and 0<=x+dx[d]*cnt<M and board[y+dy[d]*cnt][x+dx[d]*cnt] not in ('*', '#'):
                cnt += 1
            if 0<=y+dy[d]*cnt<N and 0<=x+dx[d]*cnt<M:
                if board[y+dy[d]*cnt][x+dx[d]*cnt] == '*':
                    board[y+dy[d]*cnt][x+dx[d]*cnt] = '.'
        else: # turn
            board[y][x] = diridx[now]
            if 0<=y+dy[now]<N and 0<=x+dx[now]<M and board[y+dy[now]][x+dx[now]] == '.':
                board[y][x], board[y+dy[now]][x+dx[now]] = board[y+dy[now]][x+dx[now]], board[y][x]
                tankco = (y+dy[now], x+dx[now])
    print(f'#{tc} ', end='')
    for i in range(N):
        print(''.join(board[i]))
