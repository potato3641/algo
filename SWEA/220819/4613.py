T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = []
    cost_board = [[0]*N for _ in range(3)]
    for i in range(N):
        line = input()
        cntW = line.count('W')
        cntB = line.count('B')
        cntR = line.count('R')
        cost_board[0][i] = M - cntW
        cost_board[1][i] = M - cntB
        cost_board[2][i] = M - cntR
        board.append(line)
    lineidx = [0, 1, 2]
    min_val = N*M
    while True:
        lineW = sum(cost_board[0][:lineidx[1]])
        lineB = sum(cost_board[1][lineidx[1]:lineidx[2]])
        lineR = sum(cost_board[2][lineidx[2]:])
        if min_val > lineW+lineB+lineR:
            min_val = lineW+lineB+lineR
        else:
            if lineidx[2] < N-1:
                lineidx[2] += 1
            elif lineidx[1] < lineidx[2]-1:
                lineidx[1] += 1
                lineidx[2] = lineidx[1] + 1
            else:
                break
    print(f'#{tc}', min_val)
