T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    LR = input()
    a, b = 1, 1
    for i in LR:
        if i == 'L':
            b = a + b
        else:
            a = a + b
    atemp, btemp = a+0, b+0
    while btemp!=0:
        temp = atemp%btemp
        atemp = btemp
        btemp = temp
    a /= atemp
    b /= atemp
    print(f'#{test_case} {int(a)} {int(b)}')
