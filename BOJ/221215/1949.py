import sys
sys.setrecursionlimit(10**6)
def miis(): return map(int,input().split())
def ii(): return int(input())
def DPS(cur, clr, prev):
    if DP[cur][clr] == -1:
        if clr:
            DP[cur][clr] = vills[cur]
        else:
            DP[cur][clr] = 0
        for i in board[cur]:
            if i != prev:
                if clr:
                    DP[cur][clr] += DPS(i, 0, cur)
                else:
                    DP[cur][clr] += max(DPS(i, 0, cur),DPS(i, 1, cur))
    return DP[cur][clr]
N = ii()
vills = list(miis())
board = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = miis()
    board[a-1].append(b-1)
    board[b-1].append(a-1)
DP = [[-1]*2 for _ in range(N)]
DPS(0, 0, -1)
DPS(0, 1, -1)
print(max(DP[0]))
