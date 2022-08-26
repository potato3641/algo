T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        A, B = map(int,input().split())
        board.append((A, B))
    rst = 0
    for i in range(N):
        for j in range(i+1, N):
            if (board[i][0] > board[j][0] and board[i][1] < board[j][1]) or \
                (board[i][0] < board[j][0] and board[i][1] > board[j][1]):
                rst += 1 
    print(f'#{tc}', rst)