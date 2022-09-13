def dfs(n):
    swt = len(nodes[n])
    if swt == 1:
        print(nodes[n][0], end='')
    elif swt == 2:
        dfs(int(nodes[n][1]))
        print(nodes[n][0], end='')
    elif swt == 3:
        dfs(int(nodes[n][1]))
        print(nodes[n][0], end='')
        dfs(int(nodes[n][2]))

T = 10
for tc in range(1, T+1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    nodes = dict()
    for i in range(N):
        nodes[int(board[i][0])] = board[i][1:]
    print(f'#{tc} ', end='')
    dfs(1)
    print()
