def miis(): return map(int,input().split())
def ii(): return int(input())
def minusOne(n): return n-1
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)
N, M, y, x, K = miis()
diceMove = ((1, 5, 0, 3, 4, 2), (2, 0, 5, 3, 4, 1), (3, 1, 2, 5, 0, 4), (4, 1, 2, 0, 5, 3))
dice = [0, 0, 0, 0, 0, 0]
board = [list(miis()) for _ in range(N)]
diceOrders = tuple(map(minusOne,miis()))
for d in diceOrders:
    if 0<=y+dy[d]<N and 0<=x+dx[d]<M:
        y += dy[d]
        x += dx[d]
        dice = [dice[diceMove[d][x]] for x in range(6)]
        if board[y][x]:
            dice[5], board[y][x] = board[y][x], 0
        else:
            board[y][x] = dice[5]+0
        print(dice[0])
