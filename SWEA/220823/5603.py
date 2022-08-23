T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [int(input()) for _ in range(N)]
    avg_line = sum(line)//len(line)
    rst = 0
    for i in line:
        rst += i-avg_line if i-avg_line>=0 else avg_line-i
    print(f'#{tc}', rst//2)