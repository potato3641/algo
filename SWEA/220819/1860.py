T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    sonim = sorted(list(map(int,input().split())))
    rst = True
    timer = 0
    making_time = M*1
    cnt = 0
    sonim_iter = 0
    while sonim_iter < N:
        if making_time <= timer:
            making_time += M
            cnt += K
        if sonim[sonim_iter] <= timer:
            sonim_iter += 1
            cnt -= 1
            if cnt < 0:
                rst = False
        timer += 1
    print(f'#{tc}', 'Possible' if rst else 'Impossible')
