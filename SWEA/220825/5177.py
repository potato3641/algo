T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int,input().split()))
    level = 0
    val = N
    while val:
        val //= 2
        level += 1
    board = [0]*(2**level)
    cnt = 0
    for i in line:
        cnt += 1
        idx = cnt
        board[idx] = i
        while True:
            if idx//2 and board[idx//2] > board[idx]:
                board[idx//2], board[idx] = board[idx], board[idx//2]
                idx //= 2
                continue
            else:
                break
    rst = 0
    while cnt//2:
        rst += board[cnt//2]
        cnt //= 2
    print(f'#{tc}', rst)