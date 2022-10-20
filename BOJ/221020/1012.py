import sys
sys.setrecursionlimit(10**6)
def dfs(y, x):
    if (y, x) in coboard:
        ttl = 1
    else:
        return 0
    visited.add((y, x))
    for d in range(4):
        if (y+dy[d], x+dx[d]) in coboard:
            if (y+dy[d], x+dx[d]) not in visited:
                ttl += dfs(y+dy[d], x+dx[d])
    return ttl
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int,input().split())
    coboard = [tuple(map(int,input().split())) for _ in range(K)]
    visited = set()
    rst = 0
    for i in range(M):
        for j in range(N):
            if (i, j) not in visited and dfs(i, j):
                rst += 1
    print(rst)

