T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    rst = 'NO'
    for i in range(N):
        temp = input()
        if temp.find('ooooo') != -1:
            rst = 'YES'
        board.append(list(temp))
    board = list(zip(*board))
    for i in range(N):
        temp = ''.join(board[i])
        if temp.find('ooooo') != -1:
            rst = 'YES'
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                if i+4 < N and j+4 < N and \
                   board[i+1][j+1] == 'o' and \
                   board[i+2][j+2] == 'o' and \
                   board[i+3][j+3] == 'o' and \
                   board[i+4][j+4] == 'o':
                    rst = 'YES'
                if i+4 < N and j-4 >= 0 and \
                   board[i+1][j-1] == 'o' and \
                   board[i+2][j-2] == 'o' and \
                   board[i+3][j-3] == 'o' and \
                   board[i+4][j-4] == 'o':
                    rst = 'YES'
    print(f'#{tc}', rst)