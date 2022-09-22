def miis(): return map(int,input().split())
T=int(input())
for tc in range(1, T+1):
    N, M = miis()
    contW = sorted(list(miis()))
    trucks = sorted(list(miis()))
    ttl = 0
    next_flag = True
    while len(contW) and len(trucks):
        now_cont = contW.pop()
        if next_flag:
            now_truck = trucks.pop()
        if now_truck >= now_cont:
            ttl += now_cont
            next_flag = True
        else:
            next_flag = False
    print(f'#{tc}', ttl)
