T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    line = list(map(int,input().split()))
    M %= N
    print(f'#{tc}', line[M])