def miis(): return map(int,input().split())
def ii(): return int(input())
def minusOne(n): return n-1
def pointDFS(y, x):
    global targetcnt
    for d in range(4):
        if 0<=y+dy[d]<N and 0<=x+dx[d]<M and (y+dy[d], x+dx[d]) not in visited and board[y+dy[d]][x+dx[d]] == targetval:
            targetcnt += 1
            visited.add((y+dy[d], x+dx[d]))
            pointDFS(y+dy[d], x+dx[d])
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)
N, M, K = miis()
dirList = (0, 3, 1, 2)
diceMove = ((2, 0, 5, 3, 4, 1), (1, 5, 0, 3, 4, 2), (4, 1, 2, 0, 5, 3), (3, 1, 2, 5, 0, 4))
dice = [1, 3, 4, 2, 5, 6]
board = [list(miis()) for _ in range(N)]
# dice = [dice[diceMove[d][x]] for x in range(6)]
ans = 0
y, x, d = 0, 0, 0
pointMemo = dict()
targetval = 0
targetcnt = 1
visited = set()
cnt = 0
while cnt < K:
    if 0<=y+dy[dirList[d]]<N and 0<=x+dx[dirList[d]]<M:
        y += dy[dirList[d]]
        x += dx[dirList[d]]
        if (y, x) in pointMemo:
            ans += pointMemo[(y, x)]
        else:
            targetval = board[y][x]
            targetcnt = 1
            visited = {(y, x)}
            pointDFS(y, x)
            pointMemo[(y, x)] = targetcnt*targetval
            ans += targetcnt*targetval
        dice = [dice[diceMove[dirList[d]][x]] for x in range(6)]
        if dice[5] > board[y][x]:
            d = (d+1)%4
        elif dice[5] < board[y][x]:
            d = (d-1)%4
    else:
        d = (d+2)%4
        continue
    cnt += 1
print(ans)
