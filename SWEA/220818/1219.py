def dfs(n):
    if board[101]: return
    board[100].append(n)
    if len(board[n]):
        for i in board[n]:
            if i not in board[100]:
                if i == 99:
                    board[101] = 1
                else:
                    dfs(i)
    
for tc in range(10):
    tc, N = map(int,input().split())
    line = list(map(int,input().split()))
    board = [[] for _ in range(102)]
    for i in range(len(line)//2):
        board[line[i*2]].append(line[i*2+1])
    board[101] = 0
    dfs(0)
    print(f'#{tc}', board[101])
