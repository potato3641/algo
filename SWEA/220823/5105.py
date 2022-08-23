def anyroad(roads, x, y, n):
    flag = True
    # print(x, y, n)
    if (x+1, y) in roads:
        flag = False
        roads[0].append((x, y))
        roads.remove((x+1, y))
        anyroad(roads, x+1, y, n+1)
    if (x, y+1) in roads:
        flag = False
        roads[0].append((x, y))
        roads.remove((x, y+1))
        anyroad(roads, x, y+1, n+1)
    if (x-1, y) in roads:
        flag = False
        roads[0].append((x, y))
        roads.remove((x-1, y))
        anyroad(roads, x-1, y, n+1)
    if (x, y-1) in roads:
        flag = False
        roads[0].append((x, y))
        roads.remove((x, y-1))
        anyroad(roads, x, y-1, n+1)
    if flag and board[x][y] == 3:
        global VAL
        VAL = n-1
T = int(input())
VAL = 0
for tc in range(1, T+1):
    N = int(input())
    board = []
    roads = [[]]
    VAL = 0
    for i in range(N):
        board.append(list(map(int,list(input()))))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                roads[0].append((i, j))
            elif board[i][j] != 1:
                roads.append((i, j))
    anyroad(roads, roads[0][0][0], roads[0][0][1], 0)
    print(f'#{tc}', VAL)