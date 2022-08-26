T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rst = 'No'
    for i in range(1, 10):
        if N%i==0 and 1 <= N//i <= 9:
            rst = 'Yes'
    print(f'#{tc}', rst)
