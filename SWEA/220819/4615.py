def is_othello(y, x, CLR):
    yourCLR = 1 if CLR-1 else 2
    for i in range(8):
        cntu, cntd = [-1, 0, 0, 0, -1, -1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1]
        cntl, cntr = [0, 0, -1, 0, -1, 0, -1, 0], [0, 0, 0, 1, 0, 1, 0, 1]
        target = []
        while True:
            if y + cntu[i] + cntd[i] < 0 or y + cntu[i] + cntd[i] > N \
            or x + cntl[i] + cntr[i] < 0 or x + cntl[i] + cntr[i] > N:
                a = x
                aa = cntl[i]
                aaa = cntr[i]
                break
            if board[y+cntu[i]+cntd[i]][x+cntl[i]+cntr[i]] == yourCLR:
                target.append((y+cntu[i]+cntd[i], x+cntl[i]+cntr[i]))
                if cntu[i]: cntu[i] += -1
                if cntd[i]: cntd[i] += 1
                if cntl[i]: cntl[i] += -1
                if cntr[i]: cntr[i] += 1
                continue
            else:
                if board[y+cntu[i]+cntd[i]][x+cntl[i]+cntr[i]] == CLR:
                    for j in target:
                        board[j[0]][j[1]] = CLR
                    break
                else:
                    break

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = [[0]*(N+1) for _ in range(N+1)]
    board[N//2][N//2:N//2+2] = [2, 1] # W, B
    board[N//2+1][N//2:N//2+2] = [1, 2] # B, W
    cntW, cntB = 0, 0
    for i in range(M):
        y, x, CLR = map(int,input().split())
        board[y][x] = CLR
        is_othello(y, x, CLR)
    for i in range(N+1):
        cntW += board[i].count(2)
        cntB += board[i].count(1)
    print(f'#{tc}', cntB, cntW)
