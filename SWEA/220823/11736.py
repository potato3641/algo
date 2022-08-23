T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int,input().split()))
    rst = 0
    for i in range(1,len(line)-1):
        if line[i] != max(line[i-1:i+2]) and line[i] != min(line[i-1:i+2]):
            rst += 1
    print(f'#{tc}', rst)