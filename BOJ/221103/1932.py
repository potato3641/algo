def miis(): return map(int,input().split())
def ii(): return int(input())
N = ii()
nowidx = 0
dp = [0]*N
dp[0] = ii()
for i in range(N-1):
    line = tuple(miis())
    keepdp = dp[:]
    for j in range(len(line)):
        if j-1 < 0:
            dp[j] = keepdp[j]+line[j]
        elif dp[j] == 0:
            dp[j] = keepdp[j-1]+line[j]
        else:
            dp[j] = max(keepdp[j-1],keepdp[j])+line[j]
print(max(dp))
