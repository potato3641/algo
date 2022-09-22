def miis(): return map(int,input().split())
def viewer():
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                print('1',end='')
            else:
                print('0',end='')
        print()
N, M = miis()
board = [list(miis()) for _ in range(N)]
aired = set()
target = 0
# init air
for i in range(N):
    for j in range(M):
        if i==0 or j==0 or i+1==N or j+1==M:
            aired.add((i, j))
rstime = 0
rstval = 0
while True:
    # new air
    myq = list(aired)
    while len(myq):
        y, x = myq.pop(0)
        if x-1>=0 and not board[y][x-1] and (y, x-1) not in aired: # 왼쪽
            aired.add((y, x-1))
            myq.append((y, x-1))
        if x+1<M and not board[y][x+1] and (y, x+1) not in aired: # 오른쪽
            aired.add((y, x+1))
            myq.append((y, x+1))
        if y-1>=0 and not board[y-1][x] and (y-1, x) not in aired: # 위
            aired.add((y-1, x))
            myq.append((y-1, x))
        if y+1<N and not board[y+1][x] and (y+1, x) not in aired: # 아래
            aired.add((y+1, x))
            myq.append((y+1, x))
    # new cheese
    rstval = 0
    terminated = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                rstval += 1
                if (i+1, j) in aired or (i-1, j) in aired or (i, j+1) in aired or (i, j-1) in aired:
                    board[i][j] = 0
                    terminated += 1
    rstime += 1
    if not terminated or terminated == rstval:
        break
print(rstime)
print(rstval)
