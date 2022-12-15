def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
board = list(miis())
hap = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N+1):
        hap[i][j-1] = max(board[i:j])-min(board[i:j])
dp = hap[0][:]
for i in range(2, N):
    for j in range(2, i+1):
        dp[i] = max(dp[i], dp[i-j]+hap[i-(j-1)][i])
print(dp[-1])
