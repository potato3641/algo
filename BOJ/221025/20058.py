import sys
input = sys.stdin.readline
from collections import deque
def miis(): return map(int,input().split())
def ii(): return int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, Q = miis()
# 2^N줄 보드
N = 1<<N
board = [list(miis()) for _ in range(N)]
# 단계 L 라인
line = list(miis())
for L in line:
    if L:
        tY, tX = 0, 0
        while True:
            todo = False
            visited = set()
            nowL = (1<<L)-1
            for y in range((1<<L)//2):
                for x in range(1<<L):
                    nowY, nowX = y, x
                    if (tY+nowY, tX+nowX) not in visited:
                        visited.add((tY+nowY, tX+nowX))
                        visited.add((tY+nowX, tX+nowL-nowY))
                        visited.add((tY+nowL-nowY, tX+nowL-nowX))
                        visited.add((tY+nowL-nowX, tX+nowY))
                        # print(tY, tX, nowY, nowX, nowL)
                        board[tY+nowY][tX+nowX], board[tY+nowX][tX+nowL-nowY], board[tY+nowL-nowY][tX+nowL-nowX], board[tY+nowL-nowX][tX+nowY] \
                        = board[tY+nowL-nowX][tX+nowY], board[tY+nowY][tX+nowX], board[tY+nowX][tX+nowL-nowY], board[tY+nowL-nowY][tX+nowL-nowX]
                    if len(visited) == 1<<(L*2):
                        todo = True
                        break
                if todo:
                    break
            tX += 1<<L
            if tX == N:
                tX = 0
                tY += 1<<L
                if tY == N:
                    break
    punished = set()
    for y in range(N):
        for x in range(N):
            cnt = 0
            for d in range(4):
                if 0<=y+dy[d]<N and 0<=x+dx[d]<N and board[y+dy[d]][x+dx[d]] > 0:
                    cnt += 1
            if cnt < 3 and board[y][x]>0:
                punished.add((y, x))
    for i in range(N):
        for j in range(N):
            if (i, j) in punished:
                board[i][j] -= 1
ans1 = 0
max_val = 0
visited = set()
for i in range(N):
    for j in range(N):
        if board[i][j]:
            ans1 += board[i][j]
            tempvisited = set()
            if (i, j) not in visited:
                myq = deque()
                myq.append((i, j))
                while myq:
                    y, x = myq.popleft()
                    todo = True
                    for d in range(4):
                        if 0<=y+dy[d]<N and 0<=x+dx[d]<N:
                            if board[y+dy[d]][x+dx[d]] > 0 and (y+dy[d], x+dx[d]) not in tempvisited:
                                tempvisited.add((y+dy[d], x+dx[d]))
                                myq.append((y+dy[d], x+dx[d]))
                                todo = False
                    if todo:
                        if max_val < len(tempvisited):
                            max_val = len(tempvisited)
            visited |= tempvisited
print(ans1)
print(max_val)
