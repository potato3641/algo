def miis(): return map(int,input().split())
# 0836 ~
# 1d - 10
# 1m - 40
# 3m - 100
# 1y - 300
T = int(input())
for tc in range(1, T+1):
    d1, m1, m3, y1 = miis()
    yearplan = list(miis())
    lendays = len(yearplan)
    dp = [[0]*12 for _ in range(4)]
    for i in range(4):
        for j in range(12):
            if i==0: # 1일로만
                dp[i][j] = d1*yearplan[j]
            elif i==1: # 1달도 써서
                dp[i][j] = min(dp[i-1][j],m1)
            elif i==2: # 3달도 써서
                if j>1:
                    if j==2:
                        dp[i][j] = min(sum(dp[i-1][:3]),m3)
                    else:
                        dp[i][j] = min(dp[i-1][j]+dp[i][j-1],dp[i][j-3]+m3)
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

            elif i==3: # 1년도 써서
                if j==11:
                    dp[i][j] = min(dp[i-1][j],y1)
    print(f'#{tc}', sum(dp[3]))
