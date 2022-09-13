N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
new_board = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        new_board[i][j] = board[i][j]+0
for i in range(N):
    for j in range(M):
        if i > 0 and j > 0: # both
            new_board[i][j] += max(new_board[i-1][j],new_board[i][j-1])
        elif i > 0: # up
            new_board[i][j] += new_board[i-1][j]
        elif j > 0: # left
            new_board[i][j] += new_board[i][j-1]
print(new_board[N-1][M-1])

