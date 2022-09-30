from collections import deque
def miis(): return map(int, input().split())
def ii(): return int(input())
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]
T = ii()
for tc in range(1, T+1):
    M, BCcnt = miis()
    Ainfo = list(miis())
    Binfo = list(miis())
    APinfo = [list(miis()) for _ in range(BCcnt)] # y, x C1 P1
    board = [[False]*10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            for APidx in range(BCcnt):
                y, x, c, p = APinfo[APidx]
                if abs(y-1-i)+abs(x-1-j) <= c:
                    if board[j][i]:
                        board[j][i].add(APidx)
                    else:
                        board[j][i] = {APidx}
    myq = deque()
    myq.append(((0, 0), (9, 9)))
    rst = 0
    cnt = 0
    while myq:
        Aco, Bco = myq.popleft()
        # 좌표 기반 충전소 번호 받아서
        Ay, Ax = Aco
        By, Bx = Bco
        Acharge = board[Ay][Ax]
        Bcharge = board[By][Bx]
        # 1-1 교집합된 충전소 번호가 있으면..
        if Acharge and Bcharge and Acharge & Bcharge:
            temp = []
            for i in Acharge:
                for j in Bcharge:
                    if i==j:
                        temp.append(APinfo[i][3])
                    if i!=j:
                        temp.append(APinfo[i][3]+APinfo[j][3])
            temp.sort(reverse=True)
            rst += temp[0]
        # 그 충전소를 A쓰B안쓰 / A쓰B쓰 / A안쓰B쓰 경우로 구분해서 최대값나오게
        # 1-2 교집합된 충전소 번호가 없으면..
        else:
            if Acharge:
                rst += max((APinfo[x][3] for x in Acharge))
            if Bcharge:
                rst += max((APinfo[x][3] for x in Bcharge))
        # A최대 B최대 해서 더하기
        # 2 다음 런
        if cnt == M:
            break
        myq.append(((Ay+dy[Ainfo[cnt]], Ax+dx[Ainfo[cnt]]), (By+dy[Binfo[cnt]], Bx+dx[Binfo[cnt]])))
        cnt += 1
    print(f'#{tc}', rst)
