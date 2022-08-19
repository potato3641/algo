T = int(input())
for test_case in range(1, T + 1):
    rst = ['' for _ in range(75)]
    for i in range(5):
        cnt = 0
        for j in input():
            rst[cnt*5+i] = j
            cnt += 1
    print(f'#{test_case} ',end='')
    print(''.join(rst))
