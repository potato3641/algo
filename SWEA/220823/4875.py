def anyroad(roads, x, y):
    flag = True
    # print(x, y)
    if (x+1, y) in roads:
        flag = False
        roads.remove((x+1, y))
        anyroad(roads, x+1, y)
    if (x, y+1) in roads:
        flag = False
        roads.remove((x, y+1))
        anyroad(roads, x, y+1)
    if (x-1, y) in roads:
        flag = False
        roads.remove((x-1, y))
        anyroad(roads, x-1, y)
    if (x, y-1) in roads:
        flag = False
        roads.remove((x, y-1))
        anyroad(roads, x, y-1)
    if flag and board[x][y] == 3:
        global VAL
        VAL = 1
T = int(input())
VAL = 0
for tc in range(1, T+1):
    N = int(input())
    board = []
    roads = []
    start_idx, end_idx = 0, 0
    VAL = 0
    for i in range(N):
        board.append(list(map(int,list(input()))))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start_idx = (i, j)
                roads.append((i, j))
            elif board[i][j] != 1:
                roads.append((i, j))
    anyroad(roads, start_idx[0], start_idx[1])
    print(f'#{tc}', VAL)