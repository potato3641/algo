def miis(): return map(int,input().split())
T = 10
for tc in range(1, T+1):
    N, S = miis()
    line = list(miis())
    board = dict()
    for i in range(N//2):
        if line[i*2] in board:
            board[line[i*2]].append(line[i*2+1])
        else:
            board[line[i*2]] = [line[i*2+1]]
    myq = []
    visited = []
    rst = []
    max_cnt = 0
    myq.append((S, 0))
    visited.append(S)
    while len(myq):
        target, mycnt = myq.pop(0)
        todoflag = True
        if target in board:
            for i in board[target]:
                
                if i not in visited:
                    myq.append((i, mycnt+1))
                    visited.append(i)
                    todoflag = False
        if todoflag:
            if max_cnt < mycnt:
                max_cnt = mycnt
                rst = [target]
            elif max_cnt == mycnt:
                rst.append(target)

    print(f'#{tc}', max(rst))
        
