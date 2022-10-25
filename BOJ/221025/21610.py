import sys
input = sys.stdin.readline
def miis(): return map(int,input().split())
def ii(): return int(input())
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
N, M = miis()
board = [list(miis()) for _ in range(N)]
orders = [tuple(miis()) for _ in range(M)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for D, S in orders:
    yadder, xadder = dy[D-1]*S, dx[D-1]*S
    mulcopy = []
    for y, x in clouds:
        y, x = (y+yadder)%N, (x+xadder)%N
        board[y][x] += 1
        mulcopy.append((y, x))
    clouds = []
    for y, x in mulcopy:
        cnt = 0
        for d in range(4):
            if 0 <= y+dy[d*2+1] < N and 0 <= x+dx[d*2+1] < N and board[y+dy[d*2+1]][x+dx[d*2+1]]:
                cnt += 1
        board[y][x] += cnt
    for i in range(N):
        for j in range(N): 
            if board[i][j] >= 2 and (i, j) not in mulcopy:
                board[i][j] -= 2
                clouds.append((i, j))
ans = 0
for i in range(N):
    for j in range(N):
        ans += board[i][j]
print(ans)
