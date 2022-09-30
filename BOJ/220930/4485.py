from collections import deque
import sys
sys.stdin = open('input.txt')
def miis(): return map(int, input().split())
def ii(): return int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

tc = 1
while True:
    N = ii()
    if N == 0:
        break
    board = [list(miis()) for _ in range(N)]
    coboard = [[1000*N*N]*N for _ in range(N)]
    coboard[0][0] = board[0][0]
    myq = deque()
    myq.append((0, 0))
    while myq:
        y, x = myq.popleft()
        for i in range(4):
            if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N:
                if coboard[y+dy[i]][x+dx[i]] > coboard[y][x]+board[y+dy[i]][x+dx[i]]:
                    coboard[y+dy[i]][x+dx[i]] = coboard[y][x]+board[y+dy[i]][x+dx[i]]
                    myq.append((y+dy[i], x+dx[i]))
    print(f'Problem {tc}:', coboard[N-1][N-1])
    tc += 1
