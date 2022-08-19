T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    line = list(map(int,input().split()))
    line.sort()
    print(f'#{test_case}', sum(line[-K:]))
