T = int(input())
for tc in range(1, T+1):
    line = input()
    rst = False
    S = set([x for x in range(1,14)])
    D = set([x for x in range(1,14)])
    H = set([x for x in range(1,14)])
    C = set([x for x in range(1,14)])
    for i in range(len(line)):
        if line[i] == 'S':
            if int(line[i+1:i+3]) not in S:
                break
            S.discard(int(line[i+1:i+3]))
        if line[i] == 'D':
            if int(line[i+1:i+3]) not in D:
                break
            D.discard(int(line[i+1:i+3]))
        if line[i] == 'H':
            if int(line[i+1:i+3]) not in H:
                break
            H.discard(int(line[i+1:i+3]))
        if line[i] == 'C':
            if int(line[i+1:i+3]) not in C:
                break
            C.discard(int(line[i+1:i+3]))
    else:
        rst = [len(S), len(D), len(H), len(C)]
    if rst:
        print(f'#{tc}', *rst)
    else:
        print(f'#{tc} ERROR')