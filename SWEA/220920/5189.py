def miis(): return map(int,input().split())
def dfs(visited, rst):
    global min_rst
    if len(visited)==N:
        rst += board[visited[-1]][0]
        if min_rst == -1 or min_rst > rst:
            min_rst = rst
    for i in range(1, N):
        if i not in visited and (min_rst == -1 or min_rst > rst+board[visited[-1]][i]):
            dfs(visited+[i], rst+board[visited[-1]][i])
min_rst = -1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(miis()) for _ in range(N)]
    min_rst = -1
    dfs([0], 0)
    print(f'#{tc}', min_rst)
