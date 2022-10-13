def miis(): return map(int,input().split())
def ii(): return int(input())
T = ii()
for tc in range(1, T+1):
    N, X = miis()
    board = [list(miis()) for _ in range(N)]
    ans = 0
    for _ in range(2):
        for i in range(N):
            nowh = board[i][0]
            usingcnt = -1
            icandoit = True
            for j in range(1, N):
                if nowh+1 == board[i][j]: # 높아진다면
                    if usingcnt+X >= j:
                        icandoit = False
                        break
                    usingcnt = j-1
                elif nowh == board[i][j]: # 평지라면
                    pass
                elif nowh == board[i][j]+1: # 낮아진다면
                    if usingcnt >= j or j+X > N:
                        icandoit = False
                        break
                    usingcnt = j + X - 1
                else:
                    icandoit = False
                    break
                nowh = board[i][j]
            if icandoit:
                ans += 1
            # print(icandoit)
        board = list(map(list, zip(*board)))
    print(f'#{tc}', ans)
