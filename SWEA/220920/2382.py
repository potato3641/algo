import sys
sys.stdin = open('input.txt')
def miis(): return map(int,input().split())
def viewer(coord):
    for i in range(N):
        for j in range(N):
            if (i, j) in coord:
                print('■', end='')
            else:
                print('□', end='')
        print()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    # input
    N, M, K = miis()
    cellinfo = dict()
    for _ in range(K):
        y, x, n, d = miis()
        cellinfo[(y, x)] = [n, d]
    board = [[] for _ in range(N)]
    # main
    # if tc!=2: continue
    for _ in range(M):
        now_cellinfo = cellinfo.copy()
        for target in now_cellinfo:
            n, d = cellinfo[target]
            y, x = target
            if type(d) == type([]):
                d = d.pop(0)
                n = n.pop(0)
            else:
                del cellinfo[(y, x)]
            y += dy[d-1]
            x += dx[d-1]
            if y == 0 or x == 0 or y==N-1 or x==N-1:
                # 방향 바꾸기
                if d == 2:
                    d = 1
                elif d == 4:
                    d = 3
                else:
                    d += 1
                # 군체 감소하기
                n //= 2
            if (y, x) in cellinfo:
                tn, td = cellinfo[(y, x)]
                if type(tn) == type([]):
                    tn.append(n)
                    td.append(d)
                else:
                    td = [td, d]
                    tn = [tn, n]
                cellinfo[(y, x)] = [tn, td]
            else:
                cellinfo[(y, x)] = [n, d]
        for target in cellinfo:
            n, d = cellinfo[target]
            if type(n) == type([]):
                maxn = max(n)
                targetidx = n.index(maxn)
                n = sum(n)
                d = d[targetidx]
                cellinfo[target] = [n, d]
        # print(cellinfo)
        # viewer(cellinfo)
        # print()
    rst = 0
    for target in cellinfo:
        n, d = cellinfo[target]
        rst += n
    print(f'#{tc}', rst)
