T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    line = list(map(int,input().split()))
    rst = set([i for i in range(1,N+1)])
    for i in line:
        rst.discard(i)
    rst = sorted(list(rst))
    print(f'#{test_case} ',end='')
    for i in rst:
        print(f'{i}',end=' ')
    print()
