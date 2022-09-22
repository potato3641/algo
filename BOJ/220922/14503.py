def miis(): return map(int,input().split())
def viewer():
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                print('■',end='')
            else:
                print('□',end='')
        print()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N, M = miis()
r, c, d = miis() # 0 북 1 동 2 남 3 서
board = [list(miis()) for _ in range(N)]
# 1이 벽
# 1. 현재위치 청소
# 2-1. 왼쪽 청소안함? 왼쪽 회전하고 1
# 2-2. 왼쪽 못 함? 왼쪽 회전하고 2
# 3. 다 못하면 후진하고 2
# 4. 다 못하고 뒤도 못 가면 끝
myq = [(r, c, d)]
cleancnt = 0
while len(myq):
    y, x, d = myq.pop(0)
    if board[y][x] == 0:
        board[y][x] = 2
        cleancnt += 1
    for _ in range(4):
        if board[y+dy[(d-1)%4]][x+dx[(d-1)%4]] == 0:
            d = (d-1)%4
            y += dy[d]
            x += dx[d]
            myq.append((y,x,d))
            break
        else:
            d = (d-1)%4
    else:
        y -= dy[d]
        x -= dx[d]
        if board[y][x] != 1:
            myq.append((y,x,d))
        else:
            break
print(cleancnt)
