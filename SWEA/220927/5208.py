def miis(): return map(int,input().split())
def dfs(busstop, n):
    # print(busstop, n)
    if busstop==N:
        global min_rst
        if min_rst > n:
            min_rst = n
    target = board[busstop]
    if target > N+1:
        target = N+1
    for i in range(target, busstop, -1):
        if min_rst > n+1:
            dfs(i, n+1)
min_rst = 0
T = int(input())
for tc in range(1, T+1):
    N, *line = miis()
    board = [[] for _ in range(N+1)]
    for i in range(N-1):
        if line[i] + i+1 <= N:
            board[i+1] = line[i] + i+1
        else:
            board[i+1] = N
    board[N] = -1
    min_rst = N
    dfs(1, 0)
    print(f'#{tc}', min_rst-1)
