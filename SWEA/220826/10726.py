T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    rst = 0
    for i in range(N):
        rst += M&1
        M >>= 1
    print(f'#{tc}', 'ON' if rst==N else 'OFF')