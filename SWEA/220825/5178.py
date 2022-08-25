T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())
    level = 0
    val = N
    while val:
        val //= 2
        level += 1
    one_idx = 2**(level-1)
    max_idx = 2**level-1
    board = [0]*(N+1)
    for _ in range(M):
        i, j = map(int,input().split())
        board[i] = j
    waiting = [L]
    rst = 0
    while not board[L]:
        if waiting:
            x = waiting.pop(0)
            if board[x]:
                rst += board[x]
            else:
                if x*2 <= N:
                    if not board[x*2]:
                        waiting.append(x*2)
                    else:
                        rst += board[x*2]
                if x*2+1 <= N:
                    if not board[x*2+1]:
                        waiting.append(x*2+1)
                    else:
                        rst += board[x*2+1]
        else:
            break
    print(f'#{tc}', rst)
            