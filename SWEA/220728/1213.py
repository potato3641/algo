T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    N = input()
    line = input()
    rst = 0
    while line.find(N) != -1:
        rst += 1
        line = line[(line.find(N)+len(N)):]
    print(f'#{test_case} {rst}')
