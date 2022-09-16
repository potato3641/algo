def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N, B = miis()
    clerk = list(miis())
    min_ctop = -1
    for i in range(1<<N):
        ctop = 0
        for j in range(N):
            if i&(1<<j):
                ctop += clerk[j]
        if ctop >= B:
            ctop -= B
            if min_ctop == -1 or min_ctop > ctop:
                min_ctop = ctop
    print(f'#{tc}', min_ctop)
