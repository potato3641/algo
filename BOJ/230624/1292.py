A, B = map(int,input().split())
board = []
for i in range(1, 46):
    for j in range(i):
        board.append(i)
print(sum(board[A-1:B]))
