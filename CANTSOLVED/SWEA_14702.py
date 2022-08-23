def dfs(aN, n, done):
    global RST
    if RST != -1 and RST < n:
        return
    for i in range(N):
        if aN[i] != -1 and aN[i-1]+aN[i]+aN[(i+1)%N] <= bNs[i]:
            test = aN[:]
            temp = done[:]
            test[i] += aN[(i+1)%N] + aN[i-1]
            if test[i] == bNs[i]:
                temp = done+[i]
                if len(temp) == N:
                    if RST != -1:
                        RST = min(RST, n+1)
                    else:
                        RST = n+1
                    break
            dfs(test, n+1, temp)


RST = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    aNs = list(map(int,input().split()))
    bNs = list(map(int,input().split()))
    RST = -1
    dfs(aNs, 0, [])
    print(f'#{tc}', RST)
