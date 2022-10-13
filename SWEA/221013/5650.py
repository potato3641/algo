reflected = ((2, 3, 1, 0), (1, 3, 0, 2), (3, 2, 0, 1), (2, 0, 3, 1), (2, 3, 0, 1))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    max_val = 0
    halldict = dict()
    for i in range(N):
        for j in range(N):
            if board[i][j]>5:
                if board[i][j] not in halldict.values():
                    halldict[(i, j)] = board[i][j]
                else:
                    pairkey = list(halldict.keys())[list(halldict.values()).index(board[i][j])]
                    halldict[(i, j)] = pairkey
                    halldict[pairkey] = (i, j)
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                for d in range(4):
                    y, x, rst = i+0, j+0, 0
                    while True:
                        if 0<=y+dy[d]<N and 0<=x+dx[d]<N and board[y+dy[d]][x+dx[d]]!=5:
                            if board[y+dy[d]][x+dx[d]]>5: # wormhall
                                y, x = halldict[(y+dy[d], x+dx[d])]
                            elif board[y+dy[d]][x+dx[d]]>0:
                                y += dy[d]
                                x += dx[d]
                                if (d+2)%4 == reflected[board[y][x]-1][d]:
                                    rst = rst*2+1
                                    break
                                d = reflected[board[y][x]-1][d]
                                rst += 1
                            elif board[y+dy[d]][x+dx[d]] == 0:
                                y += dy[d]
                                x += dx[d]
                            else:
                                break
                        else:
                            rst = rst*2+1
                            break
                        if (y, x) == (i, j):
                            break
                    if max_val < rst:
                        max_val = rst
    print(f'#{tc}', max_val)
