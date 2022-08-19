T = int(input())
def is_board(board, y, x):
    cnt, row, col = 0, 1, 1
    flag = 1
    while True:
        if board[y][x] and flag&1:
            board[y][x] = 0
            x += 1
            cnt += 1
        elif not board[y][x] and flag&1:
            x -= 1
            board[y][x] = 1
            col = cnt*1
            cnt = 0
            flag = 0
        if board[y][x] and flag^1:
            board[y][x+1-col:x+1] = [0]*col
            y += 1
            cnt += 1
        elif not board[y][x] and flag^1:
            y -= 1
            row = cnt*1
            break
    return board, row, col
for tc in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int,input().split())))
    data = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                board, r, c = is_board(board, i, j)
                data.append((r, c))
    data.sort(key = lambda x:(x[0]*x[1], x[0]))
    print(f'#{tc} {len(data)} ', end='')
    for i in data:
        print(*i, end=' ')
    print()
