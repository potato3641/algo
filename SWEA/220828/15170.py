def adjoingate(gnum, visited):
    target = [gnum]
    while True:
        basket = []
        for i in target:
            if i not in visited:
                basket.append(i)
        if len(basket):
            target = basket
            break
        if len(target)==1:
            x = target.pop()
            if 0 < x-1 <= N:
                target.append(x-1)
            if 0 < x+1 <= N:
                target.append(x+1)
        elif len(target)==2:
            x1 = target.pop()+1
            x2 = target.pop()-1
            if 0 < x2 <= N:
                target.append(x2)
            if 0 < x1 <= N:
                target.append(x1)
    return target
def dfs(gpri, snum, temp, rst, gcnt):
    global min_rst
    if gcnt == gate_cnt[gpri[snum]]:
        if snum == 2:
            if min_rst == 0:
                min_rst = rst
            elif min_rst > rst:
                min_rst = rst
            return
        else:
            dfs(gpri, snum+1, temp, rst, 0)
            return
    target_gnum = adjoingate(gate_set[gpri[snum]], temp)
    if len(target_gnum) == 2 and gate_cnt[gpri[snum]]-gcnt > 1 and len(set(target_gnum)-set(temp)) == 2:
        lentgnum = abs(gate_set[gpri[snum]]-target_gnum[0])+abs(gate_set[gpri[snum]]-target_gnum[1])+2
        if min_rst == 0 or lentgnum < min_rst:
            dfs(gpri, snum, temp+target_gnum, rst+lentgnum, gcnt+2)
    else:
        for i in target_gnum:
            if i not in temp:
                if min_rst == 0 or rst+abs(gate_set[gpri[snum]]-i)+1 < min_rst:
                    dfs(gpri, snum, temp+[i], rst+abs(gate_set[gpri[snum]]-i)+1, gcnt+1)
T = int(input())
min_rst = 0
gate_pri = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,1,0],[2,0,1]]
for tc in range(1, T+1):
    N = int(input())
    gates = [0]*(N+1)
    gate_set = []
    gate_cnt = []
    for _ in range(3):
        g, n = map(int,input().split())
        gate_cnt.append(n)
        gate_set.append(g)
    min_rst = 0
    for i in range(6):
        dfs(gate_pri[i], 0, [], 0, 0)
    print(f'#{tc}', min_rst)
