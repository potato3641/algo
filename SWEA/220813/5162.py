T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int,input().split())
    print(f'#{test_case} {C//(A if A < B else B)}')
