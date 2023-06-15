N, M = map(int,input().split())
board = []
for _ in range(N):
    temp = list(input())
    board.append(temp)
revboard = list(map(list,zip(*board)))
horizon = 0
vertical = 0
for i in range(N):
    if 'X' not in board[i]:
        horizon += 1
for i in range(M):
    if 'X' not in revboard[i]:
        vertical += 1
print(max(horizon,vertical))
