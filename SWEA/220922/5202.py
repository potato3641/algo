def miis(): return map(int,input().split())
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [tuple(miis()) for _ in range(N)]
    board.sort(key=lambda x: (x[1], x[0]))
    end = 0
    cnt = 0
    for i in board:
        if i[0] >= end:
            end = i[1]
            cnt += 1
    print(f'#{tc}', cnt)
