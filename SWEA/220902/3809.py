T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n = 0
    line = ''
    while True:
        temp = input().split()
        n += len(temp)
        line += ''.join(temp)
        if N==n:
            break
    cnt = 0
    while True:
        if line.find(str(cnt)) == -1:
            break
        cnt += 1
    print(f'#{test_case}', cnt)
