def miis(): return map(int,input().split())
def viewer():
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                print('1',end='')
            else:
                print('0',end='')
        print()

N, M, K = miis()
coboard = [tuple(miis()) for _ in range(K)]
board = [[1]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
target = 0
for x1, y1, x2, y2 in coboard:
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 0
            visited[i][j] = 1
for i in range(N):
    for j in range(M):
        if board[i][j]:
            target = (i, j)
            break
    if not target:
        break
rstarr = []
myq = [target]
block = 0
# viewer()
# print()
while True:
    target = myq.pop(0)
    y, x = target
    board[y][x] = 0
    block += 1
    if x-1>=0 and board[y][x-1] and not visited[y][x-1] and (y, x-1) not in myq: # 왼쪽
        visited[y][x-1] = 1
        myq.append((y, x-1))
    if x+1<M and board[y][x+1] and not visited[y][x+1] and (y, x+1) not in myq: # 오른쪽
        visited[y][x+1] = 1
        myq.append((y, x+1))
    if y-1>=0 and board[y-1][x] and not visited[y-1][x] and (y-1, x) not in myq: # 위
        visited[y-1][x] = 1
        myq.append((y-1, x))
    if y+1<N and board[y+1][x] and not visited[y+1][x] and (y+1, x) not in myq: # 아래
        visited[y+1][x] = 1
        myq.append((y+1, x))
    if not len(myq):
        # viewer()
        # print()
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    rstarr.append(block)
                    block = 0
                    myq = [(i, j)]
                    break
            if len(myq):
                break
        if len(myq):
            continue
        if len(visited):
            rstarr.append(block)
        break
rstarr.sort()
print(len(rstarr))
print(*rstarr)
