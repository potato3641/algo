T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    line = list(map(int,input().split()))
    max_line = line[0]
    min_line = line[0]
    for i in line:
        if i > max_line:
            max_line = i
        if i < min_line:
            min_line = i
    print(f'#{test_case} {max_line-min_line}')
