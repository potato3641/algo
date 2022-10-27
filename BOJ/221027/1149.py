import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
dp = [[0]*3 for _ in range(N)]
for i in range(N):
    r, g, b = miis()
    if i:
        dp[i][0] = r+min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = g+min(dp[i-1][2], dp[i-1][0])
        dp[i][2] = b+min(dp[i-1][0], dp[i-1][1])
    else:
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b
print(min(dp[N-1]))
