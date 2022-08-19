T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    line = list(map(int,input().split()))
    rst = 0
    for i in line:
        if i <= sum(line)/N:
            rst += 1
    print(f'#{test_case} {rst}')
