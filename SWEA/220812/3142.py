T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    print(f'#{test_case} {2*M-N} {N-M}')
