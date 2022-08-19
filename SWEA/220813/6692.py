T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rst = 0
    for i in range(N):
        p, x = map(float,input().split())
        rst += p*x
    print(f'#{test_case} {rst}')
