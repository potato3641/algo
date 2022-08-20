T = int(input())
for test_case in range(1, T + 1):
    line_cnt, wrap_cnt = map(int,input().split())
    line = list(map(int,input().split()))
    max_line = 0
    min_line = 0
    for i in range(line_cnt-wrap_cnt+1):
        cur_line = 0
        for j in line[i:i+wrap_cnt]:
            cur_line += j
        if not i:
            min_line = cur_line
        if cur_line > max_line:
            max_line = cur_line
        if cur_line < min_line:
            min_line = cur_line
    print(f'#{test_case} {max_line-min_line}')
