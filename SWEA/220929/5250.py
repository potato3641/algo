from collections import deque
def miis(): return map(int, input().split())
def ii(): return int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = ii()
for tc in range(1, T+1):
    N = ii()
    board = [list(miis()) for _ in range(N)]
    coboard = [[1000*N*N]*N for _ in range(N)]
    coboard[0][0] = 0
    myq = deque()
    myq.append((0, 0))
    while myq:
        y, x = myq.popleft()
        for i in range(4):
            if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N:
                addfeul = 1
                if board[y+dy[i]][x+dx[i]] > board[y][x]:
                    addfeul += board[y+dy[i]][x+dx[i]] - board[y][x]
                if coboard[y+dy[i]][x+dx[i]] > coboard[y][x]+addfeul:
                    coboard[y+dy[i]][x+dx[i]] = coboard[y][x]+addfeul
                    myq.append((y+dy[i], x+dx[i]))

    print(f'#{tc}', coboard[N-1][N-1])
