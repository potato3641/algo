T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = input()
    rst = 0
    now = 0
    for i in memory:
        rst += int((not now and int(i)) or (now and not int(i)))
        now = int(i)
    print(f'#{test_case} {rst}')
