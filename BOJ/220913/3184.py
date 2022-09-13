def bfs(s, w):
    areasheep = []
    for i, j in sheepboard:
        if (i, j) in areasheep:
            continue
        myq = []
        temp = []
        myq.append((i, j))
        temp.append((i, j))
        sheepcnt = 0
        wolfcnt = 0
        while len(myq) > 0:
            i, j = myq[-1]
            del myq[-1]
            if board[i][j] == 'o':
                sheepcnt += 1
            elif board[i][j] == 'v':
                wolfcnt += 1
            if (i, j) in sheepboard:
                areasheep.append((i, j))
            if board[i+1][j] != '#' and (i+1, j) not in temp:
                myq.append((i+1, j))
                temp.append((i+1, j))
            if board[i-1][j] != '#' and (i-1, j) not in temp:
                myq.append((i-1, j))
                temp.append((i-1, j))
            if board[i][j+1] != '#' and (i, j+1) not in temp:
                myq.append((i, j+1))
                temp.append((i, j+1))
            if board[i][j-1] != '#' and (i, j-1) not in temp:
                myq.append((i, j-1))
                temp.append((i, j-1))
        if sheepcnt > wolfcnt:
            w -= wolfcnt
        else:
            s -= sheepcnt
    return s, w
        

N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
sheepboard = []
wolf = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            sheepboard.append((i, j))
        elif board[i][j] == 'v':
            wolf += 1
print(*bfs(len(sheepboard), wolf))
