def miis(): return map(int, input().split())
def ii(): return int(input())
N, M = miis()
board = [list(map(int,tuple(input()))) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
max_val = 0
for y in range(N):
    for x in range(M):
        if board[y][x]:
            if y == 0 or x == 0:
                dp[y][x] = 1
                if max_val < dp[y][x]:
                    max_val = dp[y][x]
            else:
                if dp[y-1][x-1] == dp[y-1][x] == dp[y][x-1]:
                    dp[y][x] = dp[y-1][x-1] + 1 
                    if max_val < dp[y][x]:
                        max_val = dp[y][x]
                else:
                    dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
                
        else:
            dp[y][x] = 0
print(max_val*max_val)
