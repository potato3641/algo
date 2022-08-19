T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    N, M = map(int,input().split())
    def recFunc(N, M):
        if M == 1:
            return N
        else:
            return N * recFunc(N,M-1)
    print(f'#{test_case} {recFunc(N, M)}')
