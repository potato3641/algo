def miis(): return map(int,input().split())
T = int(input())
for tc in range(1, T+1):
    N, M = miis()
    # +1 -1 *2 -10
    myq = [(N, 0, 0)]
    visited = set()
    endflag = True
    while endflag:
        temp = myq[:]
        myq = []
        for target, cals, m1cnt in temp:
            if target == M:
                print(f'#{tc}', cals)
                endflag = False
                break
            if m1cnt > 9 or target-16 > M or target<-10 or target > 1000000:
                continue
            if target not in visited:
                visited.add(target)
                myq.append((target*2, cals+1, 0))
                myq.append((target+1, cals+1, 0))
                myq.append((target-1, cals+1, m1cnt+1))
                myq.append((target-10, cals+1, 0))
