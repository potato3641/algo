def dfs(cx, n, rst):
    global min_rst
    if rst > min_rst: return
    if n == N:
        if min_rst > rst:
            min_rst = rst
        return
    else:
        for i in range(N):
            if i not in cx:
                tx = cx + [i]
                dfs(tx, n+1, rst+nums_board[n][i])

min_rst = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums_board = []
    min_rst = 10*N
    for _ in range(N):
        nums_board.append(list(map(int,input().split())))
    dfs([], 0, 0)
    print(f'#{tc}', min_rst)
