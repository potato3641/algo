N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
coboard = []
pvirus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            coboard.append((i, j))
        elif board[i][j] == 2:
            pvirus.append((i, j))
# init set
min_cnt = -1
for i in range(len(coboard)):
    for j in range(i+1, len(coboard)):
        for k in range(j+1, len(coboard)):
            roadboard = coboard[:]
            roadboard.remove(coboard[i])
            roadboard.remove(coboard[j])
            roadboard.remove(coboard[k])
            visited = []
            myq = pvirus[:]
            # loop start
            breaker = True
            while breaker:
                temp = myq[:]
                for y, x in temp:
                    myq.remove((y,x))
                    if (y+1, x) in roadboard and (y+1, x) not in visited:
                        myq.append((y+1, x))
                        visited.append((y+1, x))
                    if (y, x+1) in roadboard and (y, x+1) not in visited:
                        myq.append((y, x+1))
                        visited.append((y, x+1))
                    if (y-1, x) in roadboard and (y-1, x) not in visited:
                        myq.append((y-1, x))
                        visited.append((y-1, x))
                    if (y, x-1) in roadboard and (y, x-1) not in visited:
                        myq.append((y, x-1))
                        visited.append((y, x-1))
                    if min_cnt != -1 and len(visited) >= min_cnt:
                        breaker = False
                        break
                if breaker:
                    if len(myq) == 0:
                        if min_cnt > len(visited) or min_cnt == -1:
                            min_cnt = len(visited)
                            # print(coboard[i], coboard[j], coboard[k], roadboard, visited)
                        breaker = False
print(len(coboard)-min_cnt-3)
