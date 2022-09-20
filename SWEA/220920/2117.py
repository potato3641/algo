def miis(): return map(int,input().split())
def serviceArea(coord, k):
    y, x = coord
    rst = set()
    for i in range(y-k, y+k+1):
        if 0 <= i < N:
            for j in range(x-k, x+k+1):
                if 0 <= j < N:
                    if abs(y-i)+abs(x-j) < k:
                        rst.add((i, j))
    return rst
def viewer(coord):
    for i in range(N):
        for j in range(N):
            if (i, j) in coord:
                print('■', end='')
            else:
                print('□', end='')
        print()
T = int(input())
for tc in range(1, T+1):
    # input
    N, M = miis()
    board = [list(miis()) for _ in range(N)]
    # setting
    houses = set()
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                houses.add((i, j))
    # print('h', houses)
    max_house = 1
    for K in range(2, 2*N):
        for i in range(N):
            for j in range(N):
                howmanyhouse = len(houses&serviceArea((i, j), K))
                if howmanyhouse*M-K*K-(K-1)*(K-1) >= 0 and max_house < howmanyhouse:
                    max_house = howmanyhouse
    print(f'#{tc}', max_house)
