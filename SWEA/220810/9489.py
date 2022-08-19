T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    rst = 0
    line = []
    for i in range(N):
        line.append(list(map(int,input().split())))
    if N<M:
        selNM = M
    else:
        selNM = N
    for i in range(selNM):
        horiz_rst, verti_rst = 0, 0
        for j in range(selNM):
            try:
                if line[i][j]:
                    horiz_rst += 1
                    if rst < horiz_rst:
                        rst = horiz_rst
                else:
                    horiz_rst = 0
            except: pass
            try:
                if line[j][i]:
                    verti_rst += 1
                    if rst < verti_rst:
                        rst = verti_rst
                else:
                    verti_rst = 0
            except: pass
                
    print(f'#{test_case} {rst}')
