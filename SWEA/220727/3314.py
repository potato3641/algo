T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = list(map(int,input().split()))
    tot = 0
    for i in line:
        if i < 40:
            i = 40
        tot += i
    print(f'#{test_case} {int(tot/5)}')
