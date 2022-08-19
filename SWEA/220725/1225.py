T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input()
    line = list(map(int,input().split()))
    cnt = 1
    while line[-1]:
        last = line[0] - cnt
        if last < 0:
            last = 0
        line = line[1:8] + [last]
        cnt += 1
        if cnt > 5: cnt = 1
    print(f'#{test_case}',end=' ')
    for i in range(8):
        print(f'{line[i]}', end=' ')
    print()
