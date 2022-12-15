def miis(): return map(int,input().split())
def ii(): return int(input())
def DPS():
    for cur in range(2, N+1, 2):
        if cur in DP:
            continue
        else:
            DP[cur] = 0
        for target in range(0, cur, 2):
            leftSide = DP[target]
            rightSide = DP[cur-target-2]
            DP[cur] += leftSide*rightSide
            DP[cur] %= 987654321
N = ii()
DP = dict()
DP[0] = 1
DPS()
print(DP[N])

