def miis(): return map(int,input().split())
def ii(): return int(input())
def sims(n):
    if n > K:
        cnt = 0
        for i in boardict:
            if boardict[i]+coboard[i]>0:
                cnt += 1
        return cnt
    else:
        nowadded = set()
        temp = list(boardict.keys())
        for i in temp:
            if boardict[i]+coboard[i]>0:
                if coboard[i] <= 0:
                    y, x = i
                    for d in range(4):
                        if (y+dy[d], x+dx[d]) in nowadded:
                            boardict[(y+dy[d], x+dx[d])] = max(boardict[(y+dy[d], x+dx[d])],boardict[i]+0)
                            coboard[(y+dy[d], x+dx[d])] = max(boardict[(y+dy[d], x+dx[d])],boardict[i]+0)
                        elif (y+dy[d], x+dx[d]) not in boardict:
                            nowadded.add((y+dy[d], x+dx[d]))
                            boardict[(y+dy[d], x+dx[d])] = boardict[i]+0
                            coboard[(y+dy[d], x+dx[d])] = boardict[i]+0
                coboard[i] -= 1
        return sims(n+1)

dy = [1,-1,0,0]
dx = [0,0,1,-1]
T = ii()
for tc in range(1, T+1):
    N, M, K = miis()
    board = [list(miis()) for _ in range(N)]
    coboard = dict()
    boardict = dict()
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                coboard[(i, j)] = board[i][j]+0
                boardict[(i, j)] = board[i][j]+0

    print(f'#{tc}', sims(1))
