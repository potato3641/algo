T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int,input().split())
    rst = 0
    for i in range(N):
        rst += D*(1+i*L/100)
    print(f'#{tc}', int(rst))