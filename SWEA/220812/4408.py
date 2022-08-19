T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [0]*200
    info_line = []
    rst = 1
    for i in range(N):
        temp_start, temp_end = map(int,input().split())
        if temp_start > temp_end:
            temp_start, temp_end = temp_end, temp_start
        temp_start = temp_start//2 if temp_start%2 else temp_start//2-1
        temp_end = temp_end//2 if temp_end%2 else temp_end//2-1
        line[temp_start:temp_end+1] = [x+1 for x in line[temp_start:temp_end+1]]
    rst = max(line)
    print(f'#{tc}', rst)
