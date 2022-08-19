T = 10
N = 16
VAL = 0
def anyroad(roads, x, y):
    flag = True
    #print(y, x)
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
    if flag and board[y][x] == 3:
        global VAL
        VAL = 1
        
for tc in range(1, T+1):
    input()
    board = []
    for _ in range(N):
        board.append(list(map(int,list(input()))))
    zip_board = list(map(list,zip(*board)))
    cutterX, cutterY = [], []
    start_point = ()
    roads = []
    for i in range(N):
        if board[i].count(1) == N:
            cutterY.append(i)
        if zip_board[i].count(1) == N:
            cutterX.append(i)
    for y in range(N):
        for x in range(N):
            if y not in cutterY and x not in cutterX:
                if board[y][x] == 2:
                    start_point = (x, y)
                if board[y][x] != 1:
                    roads.append((x, y))
    VAL = 0
    anyroad(roads, start_point[0], start_point[1])
    print(f'#{tc}', VAL)
