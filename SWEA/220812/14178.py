T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int,input().split())
    rst = N//(D*2+1) + ( 1 if N%(D*2+1) else 0 )
    print(f'#{test_case} {rst}')
