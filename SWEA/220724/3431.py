T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L, U, X = map(int,input().split())
    print(f'#{test_case} ',end='')
    if U < X:
        print(-1)
    elif X < L:
        print(L-X)
    else:
        print(0)
