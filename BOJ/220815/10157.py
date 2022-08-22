C, R = map(int,input().split())
K = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = [[0]*(C+1) for i in range(R+1)]
cnt = 1
x, y = 1, 1
x_iter, y_iter = 0, 0
if C*R < K:
    print(0)
else:
    while True:
        board[x][y] = cnt
        if 1 > x+dx[x_iter%4] or R < x+dx[x_iter%4] or \
        1 > y+dy[y_iter%4] or C < y+dy[y_iter%4] or \
        board[x+dx[x_iter%4]][y+dy[y_iter%4]]:
            x_iter += 1
            y_iter += 1
        cnt += 1
        if cnt > K:
            break
        x += dx[x_iter%4]
        y += dy[y_iter%4]
    print(y, x)
