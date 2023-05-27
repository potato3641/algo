for tc in range(1, int(input())+1):
    N = int(input())
    cnt = N
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*i+j*j<=N*N:
                cnt += 1
    print(f'#{tc}', cnt*4+1)
