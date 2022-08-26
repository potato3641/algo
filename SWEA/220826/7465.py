T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = [[] for _ in range(N+1)]
    for i in range(M):
        A, B = map(int,input().split())
        board[A].append(B)
        board[B].append(A)
    rst = 0
    for i in range(N+1):
        if len(board[i])==0:
            rst += 1
    rst -= 1
    for i in range(N+1):
        if len(board[i])==0:
            pass
        else:
            waiting = []
            for x in board[i]:
                waiting.append(x)
            while True:
                if waiting:
                    x = waiting.pop(0)
                    if len(board[x]) > 0:
                        target = []
                        for i in board[x]:
                            waiting.append(i)
                            target.append(i)
                        for i in target:
                            board[x].remove(i)
                            board[i].remove(x)
                else:
                    break
            rst += 1
    print(f'#{tc}', rst)