T = int(input())
for tc in range(1, T+1):
    E, N = map(int,input().split())
    line = list(map(int,input().split()))
    board = [[] for _ in range(E+2)]
    for i in range(E):
        board[line[i*2]].append(line[i*2+1])
    cnt = []
    i = N
    waiting = []
    while True:
        if len(waiting):
            i = waiting.pop(0)
        elif i!=N:
            break
        cnt.append(i)
        if not len(board[i]+waiting):
            break
        elif len(board[i]):
            for x in board[i]:
                waiting.append(x)
    print(f'#{tc}', len(cnt))