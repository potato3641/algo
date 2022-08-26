T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int,input().split())
    rst = D*1440+H*60+M-(11*1440+11*60+11)
    if rst >= 0:
        print(f'#{tc}', rst)
    else:
        print(f'#{tc} -1')