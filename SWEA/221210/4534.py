from collections import defaultdict
def miis(): return map(int,input().split())
def ii(): return int(input())
def DPS(cur, clr, prev):
    if not DP[cur][clr]:
        DP[cur][clr] = 1
        for i in nodeDict[cur]:
            if i != prev:
                DP[cur][clr] *= DPS(i, 0, cur)+(0 if clr else DPS(i, 1, cur))
    return DP[cur][clr]
T = ii()
for tc in range(1, T+1):
    N = ii()
    nodeDict = defaultdict(list)
    for _ in range(N-1):
        x, y = miis()
        nodeDict[x-1].append(y-1)
        nodeDict[y-1].append(x-1)
    DP = [[0]*2 for _ in range(N)]
    ans = DPS(0, 0, -1)+DPS(0, 1, -1)
    print(f'#{tc}', ans%1000000007)


