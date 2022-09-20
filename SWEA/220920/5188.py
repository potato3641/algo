def miis(): return map(int,input().split())
def dfs(i, j, visited, rst):
    if minboard[i][j] == -1 or minboard[i][j] > rst:
        minboard[i][j] = rst
    elif minboard[i][j] < rst:
        return
    if i+1 == N and j+1 == N:
        return
    if i+1 < N and (i+1, j) not in visited:
        dfs(i+1, j, visited+[(i+1, j)], rst+board[i+1][j])
    if j+1 < N and (i, j+1) not in visited:
        dfs(i, j+1, visited+[(i, j+1)], rst+board[i][j+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(miis()) for _ in range(N)]
    minboard = [[-1]*N for _ in range(N)]
    dfs(0,0,[(0, 0)],board[0][0])
    print(f'#{tc}', minboard[N-1][N-1])
