T = 10
N = 100        
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
                    roads.append((x, y))
                if board[y][x] != 1:
                    roads.append((x, y))
    VAL = 0
    trashes = []
    x, y = start_point[0], start_point[1]
    trashes.append((x, y))
    while True:
        flag = True
        if (x+1, y) in roads:
            flag = False
            trashes.append((x+1, y))
            roads.remove((x+1, y))
            if (x, y) not in trashes:
                trashes.append((x, y))
            x += 1
            continue
        if (x, y+1) in roads:
            flag = False
            trashes.append((x, y+1))
            roads.remove((x, y+1))
            if (x, y) not in trashes:
                trashes.append((x, y))
            y += 1
            continue
        if (x-1, y) in roads:
            flag = False
            trashes.append((x-1, y))
            roads.remove((x-1, y))
            if (x, y) not in trashes:
                trashes.append((x, y))
            x -= 1
            continue
        if (x, y-1) in roads:
            flag = False
            trashes.append((x, y-1))
            roads.remove((x, y-1))
            if (x, y) not in trashes:
                trashes.append((x, y))
            y -= 1
            continue
        if flag and board[y][x] == 3:
            VAL = 1
            break
        if flag:
            try:
                x, y = trashes.pop(-1)
            except IndexError:
                break
    print(f'#{tc}', VAL)
