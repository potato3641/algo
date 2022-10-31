def miis(): return map(int,input().split())
def ii(): return int(input())
def is_inboard(y, x):
    if 0<=y<N and 0<=x<N:
        return True
    return False
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
N = ii()
board = [list(miis()) for _ in range(N)]
y, x, d = (N-1)//2, (N-1)//2, 0
visited = {(y, x)}
ans = 0
while (y, x) != (0, 0):
    # 이동
    nowy, nowx = y+dy[d], x+dx[d]
    visited.add((nowy, nowx))
    # 흩날리기
    if board[nowy][nowx]:
        moray, board[nowy][nowx] = board[nowy][nowx], 0
        elsemoray = moray - (2*(moray*1//100)+2*(moray*2//100)+2*(moray*7//100)+2*(moray*10//100)+moray*5//100)
        if is_inboard(nowy+dy[d], nowx+dx[d]):
            board[nowy+dy[d]][nowx+dx[d]] += elsemoray # alpha
        else:
            ans += elsemoray
        if is_inboard(nowy+dy[d]*2, nowx+dx[d]*2):
            board[nowy+dy[d]*2][nowx+dx[d]*2] += moray*5//100 # 5%
        else:
            ans += moray*5//100
        if is_inboard(nowy+dy[d]+dy[(d+1)%4], nowx+dx[d]+dx[(d+1)%4]):
            board[nowy+dy[d]+dy[(d+1)%4]][nowx+dx[d]+dx[(d+1)%4]] += moray*10//100 # 10%
        else:
            ans += moray*10//100
        if is_inboard(nowy+dy[d]+dy[(d-1)%4], nowx+dx[d]+dx[(d-1)%4]):
            board[nowy+dy[d]+dy[(d-1)%4]][nowx+dx[d]+dx[(d-1)%4]] += moray*10//100 # 10%
        else:
            ans += moray*10//100
        if is_inboard(nowy+dy[(d+1)%4], nowx+dx[(d+1)%4]):
            board[nowy+dy[(d+1)%4]][nowx+dx[(d+1)%4]] += moray*7//100 # 7%
        else:
            ans += moray*7//100
        if is_inboard(nowy+dy[(d-1)%4], nowx+dx[(d-1)%4]):
            board[nowy+dy[(d-1)%4]][nowx+dx[(d-1)%4]] += moray*7//100 # 7%
        else:
            ans += moray*7//100
        if is_inboard(nowy-dy[d]+dy[(d+1)%4], nowx-dx[d]+dx[(d+1)%4]):
            board[nowy-dy[d]+dy[(d+1)%4]][nowx-dx[d]+dx[(d+1)%4]] += moray*1//100 # 10%
        else:
            ans += moray*1//100
        if is_inboard(nowy-dy[d]+dy[(d-1)%4], nowx-dx[d]+dx[(d-1)%4]):
            board[nowy-dy[d]+dy[(d-1)%4]][nowx-dx[d]+dx[(d-1)%4]] += moray*1//100 # 10%
        else:
            ans += moray*1//100
        if is_inboard(nowy+dy[(d+1)%4]*2, nowx+dx[(d+1)%4]*2):
            board[nowy+dy[(d+1)%4]*2][nowx+dx[(d+1)%4]*2] += moray*2//100 # 2%
        else:
            ans += moray*2//100
        if is_inboard(nowy+dy[(d-1)%4]*2, nowx+dx[(d-1)%4]*2):
            board[nowy+dy[(d-1)%4]*2][nowx+dx[(d-1)%4]*2] += moray*2//100 # 2%
        else:
            ans += moray*2//100
    # 방향체크
    if (nowy+dy[(d+1)%4], nowx+dx[(d+1)%4]) not in visited:
        d = (d+1)%4
    y, x = nowy, nowx
print(ans)
